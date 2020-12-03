from typing import Optional, Any
import asyncio

try:
    import aiohttp
except ImportError:
    aiohttp = Any

from . import types
from .utils import viber_logger, constants, exceptions


class Bot:
    """Provides work with Viber API
    """

    _loop: asyncio.AbstractEventLoop
    _session_headers: dict
    _request_headers: dict
    _session: aiohttp.ClientSession

    def __init__(
        self,
        token: str,
        loop: Optional[asyncio.AbstractEventLoop] = None,
        headers: Optional[dict] = None,
        proxy: str = None,
    ):
        """
        Authentication token:
        https://developers.viber.com/docs/api/rest-bot-api/#authentication-token

        :param token: unique and secret account identifier.

        :param loop: asyncio event loop

        :param headers: headers for session (used in every request)

        :param proxy: string, like: http://user:pass@some.proxy.com
        """
        self._set_event_loop(loop)

        if headers is None:
            headers = {}
        headers['X-Viber-Auth-Token'] = token
        self._session_headers = headers

        self._request_headers = {}

        if proxy is not None:
            self._request_headers['proxy'] = proxy

    @property
    def token(self) -> str:
        """
        :return: bot token
        """
        return self._session_headers.get('X-Viber-Auth-Token')

    @property
    def session(self) -> aiohttp.ClientSession:
        """
        Returns current aiohttp.ClientSession.
        If _session was closed returns new session.
        :return: aiohttp.ClientSession
        """
        if self._session is None:
            raise RuntimeError(f'{type(self)} session not created')
        if self._session.closed:
            self._session = self._get_new_session()
        return self._session

    async def __aenter__(self):
        """
        This is coroutine.
        Creates session for using in context manager scope

        :return: Bot object
        """
        await self.create_session()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        This is coroutine.
        Closing session after exit context manager scope
        """
        await self.close_session()

    def _set_event_loop(self, event_loop: Optional[asyncio.AbstractEventLoop] = None):
        """
        Saving asyncio.AbstractEventLoop for passing in aiohttp.ClientSession
        :param event_loop: asyncio.AbstractEventLoop or None
        :return: None
        """
        self._event_loop = event_loop

    def _get_new_session(self) -> aiohttp.ClientSession:
        """
        Creates and returns new aiohttp.ClientSession with self._session_kwargs
        :return: aiohttp.ClientSession
        """
        return aiohttp.ClientSession(
            headers=self._session_headers,
            loop=self._event_loop
        )

    async def create_session(self) -> aiohttp.ClientSession:
        """
        This is coroutine.
        Creates or recreates current aiohttp.ClientSession
        :return: aiohttp.ClientSession
        """
        await self.close_session()
        self._session = self._get_new_session()
        return self._session

    async def close_session(self) -> None:
        """
        This is coroutine.
        If current session was set and not closed it closed current session.
        :return: None
        """
        if self._session is not None and self._session.closed is False:
            await self._session.close()

    async def request(self, method: str, data: Optional[dict] = None) -> dict:
        """
        This is coroutine.

        Makes request to Viber API and then checks response

        :param method: viber api method, ex. send_message, set_webhook etc.
        :param data: data to send
        :return: response
        """
        viber_logger.debug(f' Request to Viber API. Method: {method}. Data: {data}')
        async with self.session.post(
            headers=self._request_headers,
            url=''.join([constants.API_URL, method]),
            json=data
        ) as response:
            return await check_response(method, response)

    async def set_webhook(
        self,
        url: str,
        event_types: Optional[list] = None,
        send_name: Optional[bool] = None,
        send_photo: Optional[bool] = None
    ) -> dict:
        """
        This is coroutine.

        Setting webhook to receive incoming updates

        :param url: Account webhook URL to receive callbacks & messages from users.
            Webhook URL must use SSL Note: Viber doesn’t support
            self signed certificates

        :param event_types: Indicates the types of Viber events that the
            account owner would like to be notified about.
            Don’t include this parameter in your request to get all events.
            Possible values: delivered, seen, failed, subscribed,
            unsubscribed  and conversation_started

        :param send_name: optional. Indicates whether or not the bot
            should receive the user name. Default false

        :param send_photo: optional. Indicates whether or not the bot
            should receive the user photo. Default false

        :return: response
        """
        webhook = types.Webhook(url, event_types, send_name, send_photo)
        return await self.request('set_webhook', webhook.serialize())

    async def remove_webhook(self) -> dict:
        """
        This is coroutine.

        Remove bot webhook

        :return: response
        """
        return await self.request('set_webhook')

    async def get_account_info(self) -> dict:
        """
        This is coroutine.

        Gets viber bot info

        :return: response
        """
        return await self.request('get_account_info')

    async def get_user_details(self, user_id: str) -> dict:
        """
        This is coroutine.

        Gets bot subscriber info

        :param user_id: subscriber user id
        :return: response
        """
        return await self.request('get_user_details', {'id': user_id})

    async def get_online(self, user_ids: list) -> dict:
        """
        This is coroutine.

        Gets online status of bot subscribers

        :param user_ids: list with subscribers id
        :return: response
        """
        return await self.request('get_online', {'ids': user_ids})

    async def send_message(
        self,
        receiver: str,
        text: str,
        tracking_data: Optional[str] = None,
        keyboard: Optional[types.Keyboard] = None
    ) -> dict:
        """
        This is coroutine.

        Sends text message to user.

        :param receiver: subscribed valid user id
        :param text: the text of the message
        :param tracking_data: Allow the account to track messages and user’s replies.
            Sent tracking_data value will be passed back with user’s reply.
            optional. max 4000 characters
        :param keyboard: types.Keyboard object to attach in request data
        :return: response
        """
        text_message = types.TextMessage(text, tracking_data, keyboard)
        data = {
            'receiver': receiver,
            **text_message.serialize(add_min_api_ver=True)
        }
        return await self.request('send_message', data=data)

    async def send_picture(
        self,
        receiver: str,
        media: str,
        text: Optional[str] = None,
        thumbnail: Optional[str] = None,
        tracking_data: Optional[str] = None,
        keyboard: Optional[types.Keyboard] = None
    ) -> dict:
        """
        This is coroutine.

        Sends picture to user.

        :param receiver: subscribed valid user id
        :param media: URL of the image (JPEG, PNG, non-animated GIF).
            Example: http://www.example.com/path/image.jpeg.
            Animated GIFs can be sent as URL messages or file messages.
            Max image size: 1MB on iOS, 3MB on Android.
        :param text: Description of the photo. Can be an empty string if irrelevant.
            required. Max 120 characters
        :param thumbnail: URL of a reduced size image (JPEG, PNG, GIF).
            optional. Recommended: 400x400. Max size: 100kb.
        :param tracking_data: Allow the account to track messages and user’s replies.
            Sent tracking_data value will be passed back with user’s reply.
            optional. max 4000 characters
        :param keyboard: types.Keyboard object to attach in request data
        :return: response
        """
        picture_message = types.PictureMessage(
            text,
            media,
            thumbnail,
            tracking_data,
            keyboard
        )
        return await self.request('send_message', data={
            'receiver': receiver,
            **picture_message.serialize(add_min_api_ver=True)
        })

    async def send_video(
        self,
        receiver: str,
        media: str,
        size: int,
        duration: Optional[int] = None,
        thumbnail: Optional[str] = None,
        tracking_data: Optional[str] = None,
        keyboard: Optional[types.Keyboard] = None
    ) -> dict:
        """
        This is coroutine.

        Sends video to user

        :param receiver: subscribed valid user id
        :param media: URL of the video (MP4, H264). Max size 26 MB.
            Only MP4 and H264 are supported. The URL must have a resource with a .mp4
            file extension as the last path segment.
            Example: http://www.example.com/path/video.mp4.
            The file must be
        :param size: Size of the video in bytes
        :param duration: Video duration in seconds; will be displayed to the receiver
        :param thumbnail: URL of a reduced size image (JPEG).
            Max size 100 kb. Recommended: 400x400. Only JPEG format is supported
        :param tracking_data: Allow the account to track messages and user’s replies.
            Sent tracking_data value will be passed back with user’s reply.
            optional. max 4000 characters
        :param keyboard: types.Keyboard object to attach in request data
        :return: response
        """
        video_message = types.VideoMessage(
            media,
            size,
            duration,
            thumbnail,
            tracking_data,
            keyboard
        )
        return await self.request('send_message', data={
            'receiver': receiver,
            **video_message.serialize(add_min_api_ver=True)
        })

    async def send_file(
        self,
        receiver: str,
        media: str,
        size: int,
        file_name: str,
        tracking_data: Optional[str] = None,
        keyboard: Optional[types.Keyboard] = None
    ) -> dict:
        """
        This is coroutine.

        Sends file to user

        :param receiver: subscribed valid user id
        :param media: URL of the file. Max size 50 MB.
            See forbidden file formats for unsupported file types:
            https://developers.viber.com/docs/api/rest-bot-api/#forbiddenFileFormats
        :param size: Size of the file in bytes
        :param file_name: Name of the file. File name should include extension.
            Max 256 characters (including file extension).
            Sending a file without extension or with the wrong extension
            might cause the client to be unable to open the file
        :param tracking_data: Allow the account to track messages and user’s replies.
            Sent tracking_data value will be passed back with user’s reply.
            optional. max 4000 characters
        :param keyboard: types.Keyboard object to attach in request data
        :return: response
        """
        file_message = types.FileMessage(
            media,
            size,
            file_name,
            tracking_data,
            keyboard
        )
        return await self.request('send_message', data={
            'receiver': receiver,
            **file_message.serialize(add_min_api_ver=True)
        })

    async def send_contact(
        self,
        receiver: str,
        name: str,
        phone_number: str,
        tracking_data: Optional[str] = None,
        keyboard: Optional[types.Keyboard] = None
    ) -> dict:
        """
        This is coroutine.

        Sends contact to user

        :param receiver: subscribed valid user id
        :param name: Name of the contact. Max 28 characters
        :param phone_number: Phone number of the contact. Max 18 characters
        :param tracking_data: Allow the account to track messages and user’s replies.
            Sent tracking_data value will be passed back with user’s reply.
            optional. max 4000 characters
        :param keyboard: types.Keyboard object to attach in request data
        :return: response
        """
        contact = types.Contact(name, phone_number)
        contact_message = types.ContactMessage(contact, tracking_data, keyboard)
        return await self.request('send_message', data={
            'receiver': receiver,
            **contact_message.serialize(add_min_api_ver=True)
        })

    async def send_location(
        self,
        receiver: str,
        latitude: str,
        longitude: str,
        tracking_data: Optional[str] = None,
        keyboard: Optional[types.Keyboard] = None
    ) -> dict:
        """
        This is coroutine.

        Sends location to user

        :param receiver: subscribed valid user id
        :param latitude: latitude (±90°)
        :param longitude: longitude (±180°)
        :param tracking_data: Allow the account to track messages and user’s replies.
            Sent tracking_data value will be passed back with user’s reply.
            optional. max 4000 characters
        :param keyboard: types.Keyboard object to attach in request data
        :return: response
        """
        location = types.Location(latitude, longitude)
        location_message = types.LocationMessage(location, tracking_data, keyboard)
        return await self.request('send_message', data={
            'receiver': receiver,
            **location_message.serialize(add_min_api_ver=True)
        })

    async def send_url(
        self,
        receiver: str,
        media: str,
        tracking_data: Optional[str] = None,
        keyboard: Optional[types.Keyboard] = None
    ) -> dict:
        """
        This is coroutine.

        Sends url to user

        :param receiver: subscribed valid user id
        :param media: URL. Max 2,000 characters
        :param tracking_data: Allow the account to track messages and user’s replies.
            Sent tracking_data value will be passed back with user’s reply.
            optional. max 4000 characters
        :param keyboard: types.Keyboard object to attach in request data
        :return: response
        """
        url_message = types.UrlMessage(media, tracking_data, keyboard)
        return await self.request('send_message', data={
            'receiver': receiver,
            **url_message.serialize(add_min_api_ver=True)
        })

    async def send_sticker(
        self,
        receiver: str,
        sticker_id: int,
        tracking_data: Optional[str] = None,
        keyboard: Optional[types.Keyboard] = None
    ) -> dict:
        """
        This is coroutine.

        Sends sticker to user

        :param receiver: subscribed valid user id
        :param sticker_id: Unique Viber sticker ID.
            For examples visit the sticker IDs page:
            https://developers.viber.com/docs/tools/sticker-ids
        :param tracking_data: Allow the account to track messages and user’s replies.
            Sent tracking_data value will be passed back with user’s reply.
            optional. max 4000 characters
        :param keyboard: types.Keyboard object to attach in request data
        :return: response
        """
        sticker_message = types.StickerMessage(sticker_id, tracking_data, keyboard)
        return await self.request('send_message', data={
            'receiver': receiver,
            **sticker_message.serialize(add_min_api_ver=True)
        })

    async def send_rich_media(
        self,
        receiver,
        rich_media: types.RichMedia,
        tracking_data: Optional[str] = None,
        keyboard: Optional[types.Keyboard] = None
    ) -> dict:
        """
        This is coroutine.

        Sends Rich Media to user.
        More info:
        https://developers.viber.com/docs/api/rest-bot-api/
        #rich-media-message--carousel-content-message

        :param receiver: subscribed valid user id
        :param rich_media: types.RichMedia object
        :param tracking_data: Allow the account to track messages and user’s replies.
            Sent tracking_data value will be passed back with user’s reply.
            optional. max 4000 characters
        :param keyboard: types.Keyboard object to attach in request data
        :return: response
        """
        rich_media_message = types.RichMediaMessage(rich_media, tracking_data, keyboard)
        return await self.request('send_message', data={
            'receiver': receiver,
            **rich_media_message.serialize(add_min_api_ver=True)
        })

    async def send_broadcast(
        self,
        broadcast_list: list,
        message: types.Message
    ) -> dict:
        """
        This is coroutine.

        Sends message to many users.
        Every user must be subscribed and have a valid user id.
        The maximum list length is 300 receivers.

        :param broadcast_list: list with subscribers id
        :param message: type.Message object
        :return: response
        """
        return await self.request('send_message', data={
            'broadcast_list': broadcast_list,
            **message.serialize(add_min_api_ver=True)
        })


def get_status_description(status_code: int) -> dict:
    """
    returns description of response code.

    :param status_code: int - status code from response
    :return: dict with status code, message, description
    """
    status = constants.ALL_STATUS_CODES.get(status_code)
    return {
        "code": status_code,
        "message": "General error" if status is None else status[0],
        "description": "General error" if status is None else status[1],
    }


async def check_response(method: str, response) -> dict:
    """
    This is coroutine.

    Checks response after request before response is closes

    :param method: api method
    :param response: aiohttp.client_reqrep.ClientResponse response from api request
    :return: dict - response json
    :raises: ApiHttpException if response code not 200
    :raises: ApiInvalidJsonException if response not contain json body
    :raises: ApiViberException if json response contain viber api error
    """
    try:
        response_json = await response.json()
    except ValueError:
        if response.status != 200:
            raise exceptions.ApiHttpException(
                response.status,
                response.reason,
                await response.text()
            )
        else:
            raise exceptions.ApiInvalidJsonException(await response.text())
    else:
        if response_json['status'] != 0:
            raise exceptions.ApiViberException(
                method,
                get_status_description(response_json['status'])
            )
        return response_json
