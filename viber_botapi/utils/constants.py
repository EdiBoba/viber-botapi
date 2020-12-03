API_URL = 'https://chatapi.viber.com/pa/'

EVENT_TYPES = (
    'delivered',
    'seen',
    'failed',
    'subscribed',
    'unsubscribed',
    'conversation_started',
)

FORBIDDEN_FORMATS = {
    'action': ('Automator Action', 'Mac OS'),
    'APK': ('Application', 'Android'),
    'APP': ('Executable', 'Mac OS'),
    'BAT': ('Batch File', 'Windows'),
    'BIN': ('Binary Executable', 'Windows, Mac OS, Linux'),
    'CMD': ('Command Script', 'Windows'),
    'COM': ('Command File', 'Windows'),
    'COMMAND': ('Terminal Command', 'Mac OS'),
    'CPL': ('Control Panel Extension', 'Windows'),
    'CSH': ('C Shell Script', 'Mac OS, Linux'),
    'EXE': ('Executable', 'Windows'),
    'GADGET': ('Windows Gadget', 'Windows'),
    'INF1': ('Setup Information File', 'Windows'),
    'INS': ('Internet Communication Settings', 'Windows'),
    'INX': ('InstallShield Compiled Script', 'Windows'),
    'IPA': ('Application', 'iOS'),
    'ISU': ('InstallShield Uninstaller Script', 'Windows'),
    'JOB': ('Windows Task Scheduler Job File', 'Windows'),
    'JSE': ('JScript Encoded File', 'Windows'),
    'KSH': ('Unix Korn Shell Script', 'Linux'),
    'LNK': ('File Shortcut', 'Windows'),
    'MSC': ('Microsoft Common Console Document', 'Windows'),
    'MSI': ('Windows Installer Package', 'Windows'),
    'MSP': ('Windows Installer Patch', 'Windows'),
    'MST': ('Windows Installer Setup Transform File', 'Windows'),
    'OSX': ('Executable', '	Mac OS'),
    'OUT': ('Executable', 'Linux'),
    'PAF': ('Portable Application Installer File', 'Windows'),
    'PIF': ('Program Information File', 'Windows'),
    'PRG': ('Executable', 'GEM'),
    'PS1': ('Windows PowerShell Cmdlet', 'Windows'),
    'REG': ('Registry Data File', 'Windows'),
    'RGS': ('Registry Script', 'Windows'),
    'RUN': ('Executable', 'Linux'),
    'SCT': ('Windows Scriptlet', 'Windows'),
    'SHB': ('Windows Document Shortcut', 'Windows'),
    'SHS': ('Shell Scrap Object', 'Windows'),
    'U3P': ('U3 Smart Application', 'Windows'),
    'VB': ('VBScript File', 'Windows'),
    'VBE': ('VBScript Encoded Script', 'Windows'),
    'VBS': ('VBScript File', 'Windows'),
    'VBSCRIPT': ('Visual Basic Script', 'Windows'),
    'WORKFLOW': ('Automator Workflow', 'Mac OS'),
    'WS': ('Windows Script', 'Windows'),
    'WSF': ('Windows Script', 'Windows'),
}

ALL_STATUS_CODES = {
    0: ('ok', 'Success'),
    1: ('invalidUrl', 'The webhook URL is not valid'),
    2: ('invalidAuthToken', 'The authentication token is not valid'),
    3: ('badData',
        'There is an error in the request itself (missing comma, brackets, etc.)'),
    4: ('missingData', 'Some mandatory data is missing'),
    5: ('receiverNotRegistered', 'The receiver is not registered to Viber'),
    6: ('receiverNotSubscribed', 'The receiver is not subscribed to the account'),
    7: ('publicAccountBlocked', 'The account is blocked'),
    8: ('publicAccountNotFound',
        'The account associated with the token is not a account.'),
    9: ('publicAccountSuspended', 'The account is suspended'),
    10: ('webhookNotSet', 'No webhook was set for the account'),
    11: (
        'receiverNoSuitableDevice',
        'The receiver is using a device or a Viber version that don’t support accounts',
    ),
    12: ('tooManyRequests', 'Rate control breach'),
    13: (
        'apiVersionNotSupported',
        'Maximum supported account version by all \
    user’s devices is less than the minApiVersion in the message',
    ),
    14: (
        'incompatibleWithVersion',
        'minApiVersion is not compatible to the message fields',
    ),
    15: ('publicAccountNotAuthorized', 'The account is not authorized'),
    16: ('inchatReplyMessageNotAllowed', 'Inline message not allowed'),
    17: ('publicAccountIsNotInline', 'The account is not inline'),
    18: (
        'noPublicChat',
        'Failed to post to public account. The bot is missing a Public Chat interface',
    ),
    19: ('cannotSendBroadcast', 'Cannot send broadcast message'),
    20: ('broadcastNotAllowed', 'Attempt to send broadcast message from the bot'),
}

PICTURE_EXTENSIONS = ('jpeg', 'png', 'gif')

INPUT_FIELD_SIZES = ('regular', 'minimized', 'hidden')

SCALE_TYPES = ('crop', 'fill', 'fit')

ACTION_TYPES = ('reply', 'open-url', 'location-picker', 'share-phone', 'none')

INTERNAL_BROWSER_ACTION_BUTTON_TYPES = (
    'forward',
    'send',
    'open-externally',
    'send-to-bot',
    'none'
)

INTERNAL_BROWSER_TITLE_TYPES = ('domain', 'default')

INTERNAL_BROWSER_MODES = (
    'fullscreen',
    'fullscreen-portrait',
    'fullscreen-landscape',
    'partial-size'
)

INTERNAL_BROWSER_FOOTER_TYPES = ('default', 'hidden')

TEXT_V_ALIGNS = ('top', 'middle', 'bottom')

TEXT_H_ALIGNS = ('left', 'center', 'right')

TEXT_SIZES = ('small', 'regular', 'large')

OPEN_URL_TYPES = ('internal', 'external')

OPEN_URL_MEDIA_TYPES = ('not-media', 'video', 'gif', 'picture')

FAVORITES_METADATA_TYPES = ('gif', 'link', 'video')
