#!/usr/bin/env python
# coding: utf-8
# vim: set ts=4 sw=4 et:

#
# Logentries Agent <https://logentries.com/>.
#

#
# Constants
#

from utils import *
from __init__ import __version__

CORP = "logentries"

NOT_SET = None

# Default user and agent keys of none are defined in configuration
DEFAULT_USER_KEY = NOT_SET
DEFAULT_AGENT_KEY = NOT_SET

# Configuration files
CONFIG_DIR_SYSTEM = '/etc/le'
CONFIG_DIR_USER = '.le'
LE_CONFIG = 'config' # Default configuration file
CONF_SUFFIX = '.conf' # Expected suffix of configuration files

LOCAL_CONFIG_DIR_USER = '.le'
LOCAL_CONFIG_DIR_SYSTEM = '/etc/le'

PID_FILE = '/var/run/logentries.pid'

MAIN_SECT = 'Main'
USER_KEY_PARAM = 'user-key'
AGENT_KEY_PARAM = 'agent-key'
FILTERS_PARAM = 'filters'
FORMATTERS_PARAM = 'formatters'
FORMATTER_PARAM = 'formatter'
ENTRY_IDENTIFIER_PARAM = 'entry_identifier'
SUPPRESS_SSL_PARAM = 'suppress_ssl'
USE_CA_PROVIDED_PARAM = 'use_ca_provided'
FORCE_DOMAIN_PARAM = 'force_domain'
DATAHUB_PARAM = 'datahub'
SYSSTAT_TOKEN_PARAM = 'system-stat-token'
STATE_FILE_PARAM = 'state-file'
HOSTNAME_PARAM = 'hostname'
TOKEN_PARAM = 'token'
PATH_PARAM = 'path'
INCLUDE_PARAM = 'include'
DESTINATION_PARAM = 'destination'
PULL_SERVER_SIDE_CONFIG_PARAM = 'pull-server-side-config'
KEY_LEN = 36
ACCOUNT_KEYS_API = '/agent/account-keys/'
ID_LOGS_API = '/agent/id-logs/'

LINE_SEPARATOR = '\xe2\x80\xa8'.decode('utf8')

PROXY_TYPE_PARAM = "proxy-type"
PROXY_URL_PARAM = "proxy-url"
PROXY_PORT_PARAM = "proxy-port"

# Maximal queue size for events sent
SEND_QUEUE_SIZE = 32000

# Logentries server details
LE_SERVER_API = '/'

LE_DEFAULT_SSL_PORT = 20000
LE_DEFAULT_NON_SSL_PORT = 10000

# Maximal pattern priority
MAX_PATTERN_PRIORITY = 100000

# Structures embedded (technology preview)
EMBEDDED_STRUCTURES = {
    # JSON with support for nested objects
    "json": "444e607f-14bd-405e-a2ce-c4892b5a3b15",
    # General kvp parser
    "kvp": "380d3f36-1a8d-45ad-972f-3001768870ca",
    # Apache access log
    "http": "803fe7ba-bd2e-44bd-8ee7-f02fa253ef5f",
}

# '--multilog' option related
# Max number of files that are allowed to be followed at any one time
MAX_FILES_FOLLOWED = 100
# Prefix used to distinguish pathnames in config or server side
# as intended for mutlilog behaviour
PREFIX_MULTILOG_FILENAME = "Multilog:"
# Time interval to retry glob of multilog pathname to catch any
# change in relevant directories that may have been deleted or added
RETRY_GLOB_INTERVAL = 0.250 # in seconds
# Intervals for .join() on several threads
FOLLOWMULTI_JOIN_INTERVAL = 1.0  # in seconds
FOLLOWER_JOIN_INTERVAL = 1.0    # in seconds
TRANSPORT_JOIN_INTERVAL = 1.5   # in seconds

class Domain(object):

    """ Logentries domains. """
    # General domains
    MAIN = 'logentries.com'
    API = 'api.logentries.com'
    DATA = 'data.logentries.com'
    PULL = 'pull.logentries.com'
    # Local debugging
    MAIN_LOCAL = '127.0.0.1'
    API_LOCAL = '127.0.0.1'
    DATA_LOCAL = '127.0.0.1'
    LOCAL = '127.0.0.1'


CONTENT_LENGTH = 'content-length'

# Log root directory
LOG_ROOT = '/var/log'

# Timeout after server connection fail. Might be a temporary network
# failure.
SRV_RECON_TIMEOUT = 10  # in seconds
SRV_RECON_TO_MIN = 1   # in seconds
SRV_RECON_TO_MAX = 10  # in seconds

# Timeout after invalid server response. Might be a version mishmash or
# temporary server/network failure
INV_SRV_RESP_TIMEOUT = 30  # Seconds

# Time interval between re-trying to open log file
REOPEN_TRY_INTERVAL = 1  # Seconds

# Number of lines which can be sent in one buck, piggybacking
MAX_LINES_SENT = 10

# Time in seconds spend between log re-checks
TAIL_RECHECK = 0.2  # Seconds

# Number of attemps to read a file, until the name is recheck
NAME_CHECK = 4  # TAIL_RECHECK cycles

# Interval of inactivity when IAA token is sent
IAA_INTERVAL = 10.0 # Seconds
# I am alive token that's passed at fixed interval during inactivity
IAA_TOKEN = "###LE-IAA###"

# Maximal size of a block of events
MAX_BLOCK_SIZE = 65536 - 512 # Space for formatting

# Interval between attampts to open a file
REOPEN_INT = 1  # Seconds

# Linux block devices
SYS_BLOCK_DEV = '/sys/block/'
# Linux CPU stat file
CPUSTATS_FILE = '/proc/stat'
# Linux mmeory stat file
MEMSTATS_FILE = '/proc/meminfo'
# Linux network stat file
NETSTATS_FILE = '/proc/net/dev'

# List of accepted network devices
NET_DEVICES = ['  eth', ' wlan', 'venet', ' veth']

EPOCH = 5  # in seconds

QUEUE_WAIT_TIME = 1  # time in seconds to wait for reading from the transport queue if it is empty


# File Handler Positions
FILE_BEGIN = 0
FILE_CURRENT = 1
FILE_END = 2

# Config response parameters
CONF_RESPONSE = 'response'
CONF_REASON = 'reason'
CONF_LOGS = 'logs'
CONF_SERVERS = 'servers'
CONF_OK = 'ok'

# Server requests
RQ_WORKLOAD = 'push_wl'

# Release information on LSB systems
LSB_RELEASE = '/etc/lsb-release'


#
# Usage help
#

PULL_USAGE = "pull <path> <when> <filter> <limit>"
PUSH_USAGE = "push <file> <path> <log-type>"
USAGE = "Logentries agent version " + __version__ + """
usage: le COMMAND [ARGS]

Where command is one of:
  init      Write local configuration file
  reinit    As init but does not reset undefined parameters
  register  Register this host
    --name=  name of the host
    --hostname=  hostname of the host
  whoami    Displays settings for this host
  monitor   Monitor this host
  follow <filename>  Follow the given log
    --name=  name of the log
    --type=  type of the log
    --multilog option used with directory wildcard * (restricted behaviour)
  followed <filename>  Check if the file is followed
  clean     Removes configuration file
  ls        List internal filesystem and settings: <path>
  rm        Remove entity: <path>
  pull      Pull log file: <path> <when> <filter> <limit>

  Structure management (technology preview)
  ls structures          List structures defined
  add structure <name>
  add structures/<name>  Add a new structure
  rm structure <name>
  rm structures/<name>   Remove a structure
  add structures/<name> <pattern> [priority]
    Add a pattern in a structure
    name          structure name
    pattern       pattern
    priority      priority of the pattern (defining ordering)
  rm structures/<name> <pattern>
                         Remove a pattern from structure
    name          structure name
    pattern       pattern to remove, alternatively beginning or ID of a pattern to remove

Where parameters are:
  --help                  show usage help and exit
  --version               display version number and exit
  --config=               load specified configuration
  --config.d=             load configurations from directory
  --account-key=          set account key and exit
  --host-key=             set local host key and exit, generate key if key is empty
  --no-timestamps         no timestamps in agent reportings
  --force                 force given operation
  --suppress-ssl          do not use SSL with API server
  --yes                   always respond yes
  --datahub               send logs to the specified data hub address
                          the format is address:port with port being optional
  --system-stat-token=    set the token for system stats log (beta)
  --pull-server-side-config=False do not use server-side config for following files
"""

# Multilog option usage
MULTILOG_USAGE = \
"""
Usage:
  Agent is expecting a path name for a file, which should be between single quotes:
        example: \'/var/log/directoryname/file.log\'
  A * wildcard for expansion of directory name can be used. Only the one * wildcard is allowed.
  Wildcard can not be used for expansion of filename, but for directory name only.
  Place path name with wildcard between single quotes:
        example: \"/var/log/directory*/file.log\"
"""

def print_usage(version_only=False):
    if version_only:
        report(__version__)
    else:
        report(USAGE)

    sys.exit(EXIT_HELP)


#
# Libraries
#

# Do not remove - fix for Python #8484
try:
    import hashlib
except ImportError:
    pass

import ConfigParser
import Queue
import atexit
import datetime
import fileinput
import getopt
import getpass
import glob
import httplib
import logging
import os
import os.path
import platform
import random
import re
import signal
import socket
import stat
import string
import subprocess
import sys
import threading
import time
import traceback
import urllib
import logging.handlers
from backports import CertificateError, match_hostname

import formats
import metrics
import socks

# Option to avoid issues around encodings
#reload(sys)
#sys.setdefaultencoding('utf8')


# Explicitely set umask to allow user rw + group read
os.umask(stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH | stat.S_IXOTH)

#
# Start logging
#

log = logging.getLogger(LOG_LE_AGENT)
if not log:
    report("Cannot open log output")
    sys.exit(EXIT_ERR)

log.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(logging.Formatter("%(message)s"))
log.addHandler(stream_handler)


def debug_filters(msg, *args):
    if config.debug_filters:
        print >> sys.stderr, msg % args

def debug_formatters(msg, *args):
    if config.debug_formatters:
        print >> sys.stderr, msg % args

#
# Imports that may not be available
#

try:
    import json

    try:
        json_loads = json.loads
        json_dumps = json.dumps
    except AttributeError:
        json_loads = json.read
        json_dumps = json.write
except ImportError:
    try:
        import simplejson
    except ImportError:
        die('NOTE: Please install Python "simplejson" package (python-simplejson) or a newer Python (2.6).')
    json_loads = simplejson.loads
    json_dumps = simplejson.dumps

class LegacySslWrapper(object):
    """Wrapper around legacy SSL support in Python 2.4. We mimic certain
    socket's functions."""

    def __init__(self, sock):
        self._socket = socket.ssl(sock)

    def send(self, data):
        self._socket.write(data)

    def close(self):
        self._socket.close()

no_ssl = False
FEAT_SSL = True
try:
    import ssl

    wrap_socket = ssl.wrap_socket
    CERT_REQUIRED = ssl.CERT_REQUIRED

except ImportError:
    no_ssl = True
    FEAT_SSL = False

    try:
        _ = httplib.HTTPSConnection
    except AttributeError:
        die('NOTE: Please install Python "ssl" module.')

    def wrap_socket(sock, ca_certs=None, cert_reqs=None):
        return LegacySslWrapper(sock)

    CERT_REQUIRED = 0

#
# Custom proctitle
#


#
# User-defined filtering code
#

def filter_events(events):
    """
    User-defined filtering code. Events passed are about to be sent to
    logentries server. Make the required modifications to the events such
    as removing unwanted or sensitive information.
    """
    # By default, this method is empty
    return events


def default_filter_filenames(filename):
    """
    By default we allow to follow any files specified in the configuration.
    """
    return True

def format_entries(default_formatter, entries):
    """
    User-defined formattering code. Events passed are about to be sent to
    logentries server. Make the required modifications to provide correct format.
    """
    # By default, this method is empty
    return default_formatter.format_line(entries)


def call(command):
    """
    Calls the given command in OS environment.
    """
    output = subprocess.Popen(
        command, stdout=subprocess.PIPE, shell=True).stdout.read()
    if len(output) == 0:
        return ''
    if output[-1] == '\n':
        output = output[:-1]
    return output


def uniq(arr):
    """
    Returns the list with duplicate elements removed.
    """
    return list(set(arr))


def _lock_pid_file_name():
    """
    Returns path to a file for protecting critical section
    for daemonizing (see daemonize() )
    """
    return config.pid_file + '.lock'


def _lock_pid():
    """
    Tries to exclusively open file for protecting of critical section
    for daemonizing.
    """
    file_name = _lock_pid_file_name()
    try:
        fd = os.open(file_name, os.O_WRONLY | os.O_CREAT | os.O_EXCL)
    except OSError:
        return None
    if fd == -1:
        return None
    os.close(fd)
    return True


def _unlock_pid():
    """
    Releases file for protecting of critical section for daemonizing.
    """
    try:
        file_name = _lock_pid_file_name()
        os.remove(file_name)
    except OSError:
        pass


def _try_daemonize():
    """
    Creates a daemon from the current process.
    http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/
    Alternative: python-daemon
    """

    try:
        pidfile = file(config.pid_file, 'r')
        pid = int(pidfile.read().strip())
        pidfile.close()
    except IOError:
        pid = None
    if pid:
        if not os.path.exists('/proc') or os.path.exists("/proc/%d/status" % pid):
            return "Pidfile %s already exists. Daemon already running?" % config.pid_file

    try:
        # Open pid file
        if config.pid_file:
            file(config.pid_file, 'w').close()

        pid = os.fork()
        if pid > 0:
            sys.exit(EXIT_OK)
        os.chdir("/")
        os.setsid()
        os.umask(0)
        pid = os.fork()
        if pid > 0:
            sys.exit(EXIT_OK)
        sys.stdout.flush()
        sys.stderr.flush()
        si = file('/dev/null', 'r')
        so = file('/dev/null', 'a+')
        se = file('/dev/null', 'a+', 0)
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # Write pid file
        if config.pid_file:
            pid = str(os.getpid())
            pidfile = file(config.pid_file, 'w')
            atexit.register(rm_pidfile)
            pidfile.write("%s\n" % pid)
            pidfile.close()
    except OSError, e:
        rm_pidfile(config)
        return "Cannot daemonize: %s" % e.strerror
    return None


def daemonize():
    """
    Creates a daemon from the current process.

    It uses helper file as a lock and then checks inside critical section
    whether pid file contains pid of a valid process.
    If not then it daemonizes itself, otherwise it dies.
    """
    if not _lock_pid():
        die("Daemon already running. If you are sure it isn't please remove %s" %
            _lock_pid_file_name())
    err = _try_daemonize()
    _unlock_pid()
    if err:
        die("%s" % err)

    # Logging for daemon mode
    log.removeHandler(stream_handler)
    shandler = logging.StreamHandler()
    shandler.setLevel(logging.DEBUG)
    shandler.setFormatter(logging.Formatter("%(asctime)s  %(message)s"))
    log.addHandler(shandler)


def print_total(elems, name):
    """
    Prints total number of elements in the list
    """
    total = len(elems)
    if total == 0:
        report("no %ss" % name)
    elif total == 1:
        report("1 " + name)
    else:
        report("%d %ss" % (total, name))


def collect_log_names(system_info):
    """
    Collects standard local logs and identifies them.
    """
    logs = []
    for root, _, files in os.walk(LOG_ROOT):
        for name in files:
            if name[-3:] != '.gz' and re.match(r'.*\.\d+$', name) is None:
                logs.append(os.path.join(root, name))

    log.debug("Collected logs: %s", logs)
    try:
        c = httplib.HTTPSConnection(LE_SERVER_API)
        request = {
            'logs': json_dumps(logs),
            'distname': system_info['distname'],
            'distver': system_info['distver']
        }
        log.debug("Requesting %s", request)
        c.request('post', ID_LOGS_API, urllib.urlencode(request), {})
        response = c.getresponse()
        if not response or response.status != 200:
            die('Error: Unexpected response from logentries (%s).' %
                response.status)
        data = json_loads(response.read())
        log_data = data['logs']

        log.debug("Identified logs: %s", log_data)
    except socket.error, msg:
        die('Error: Cannot contact server, %s' % msg)
    except ValueError, msg:
        die('Error: Invalid response from the server (Parsing error %s)' % msg)
    except KeyError:
        die('Error: Invalid response from the server, log data not present.')

    return log_data


def lsb_release(system_info):
    # General LSB system
    if os.path.isfile(LSB_RELEASE):
        try:
            fields = dict((a.split('=') for a in rfile(LSB_RELEASE).split('\n') if len(a.split('=')) == 2))
            system_info['distname'] = fields['DISTRIB_ID']
            system_info['distver'] = fields['DISTRIB_RELEASE']
            return True
        except ValueError:
            pass
        except KeyError:
            pass

    # Information not found
    return False


def release_test(filename, distname, system_info):
    if os.path.isfile(filename):
        system_info['distname'] = distname
        system_info['distver'] = rfile(filename)
        return True
    return False


def system_detect(details):
    """
    Detects the current operating system. Returned information contains:
        distname: distribution name
        distver: distribution version
        kernel: kernel type
        system: system name
        hostname: host name
    """
    uname = platform.uname()
    sys = uname[0]
    system_info = dict(system=sys, hostname=socket.getfqdn(),
                       kernel='', distname='', distver='')

    if not details:
        return system_info

    if sys == "SunOS":
        system_info['distname'] = call('cat /etc/product | sed -n "s/Name: \\(.*\\)/\\1/p"')
        system_info['distver'] = call('cat /etc/product | sed -n "s/Image: \\(.*\\)/\\1/p"')
        system_info['kernel'] = uname[2]
    elif sys == "AIX":
        system_info['distver'] = call("oslevel -r")
    elif sys == "Darwin":
        system_info['distname'] = call("sw_vers -productName")
        system_info['distver'] = call("sw_vers -productVersion")
        system_info['kernel'] = uname[2]

    elif sys == "Linux":
        system_info['kernel'] = uname[2]
        # XXX CentOS?
        releases = [
            ['/etc/debian_version', 'Debian'],
            ['/etc/UnitedLinux-release', 'United Linux'],
            ['/etc/annvix-release', 'Annvix'],
            ['/etc/arch-release', 'Arch Linux'],
            ['/etc/arklinux-release', 'Arklinux'],
            ['/etc/aurox-release', 'Aurox Linux'],
            ['/etc/blackcat-release', 'BlackCat'],
            ['/etc/cobalt-release', 'Cobalt'],
            ['/etc/conectiva-release', 'Conectiva'],
            ['/etc/fedora-release', 'Fedora Core'],
            ['/etc/gentoo-release', 'Gentoo Linux'],
            ['/etc/immunix-release', 'Immunix'],
            ['/etc/knoppix_version', 'Knoppix'],
            ['/etc/lfs-release', 'Linux-From-Scratch'],
            ['/etc/linuxppc-release', 'Linux-PPC'],
            ['/etc/mandriva-release', 'Mandriva Linux'],
            ['/etc/mandrake-release', 'Mandrake Linux'],
            ['/etc/mandakelinux-release', 'Mandrake Linux'],
            ['/etc/mklinux-release', 'MkLinux'],
            ['/etc/nld-release', 'Novell Linux Desktop'],
            ['/etc/pld-release', 'PLD Linux'],
            ['/etc/redhat-release', 'Red Hat'],
            ['/etc/slackware-version', 'Slackware'],
            ['/etc/e-smith-release', 'SME Server'],
            ['/etc/release', 'Solaris SPARC'],
            ['/etc/sun-release', 'Sun JDS'],
            ['/etc/SuSE-release', 'SuSE'],
            ['/etc/sles-release', 'SuSE Linux ES9'],
            ['/etc/tinysofa-release', 'Tiny Sofa'],
            ['/etc/turbolinux-release', 'TurboLinux'],
            ['/etc/ultrapenguin-release', 'UltraPenguin'],
            ['/etc/va-release', 'VA-Linux/RH-VALE'],
            ['/etc/yellowdog-release', 'Yellow Dog'],
        ]

        # Check for known system IDs
        for release in releases:
            if release_test(release[0], release[1], system_info):
                break
        # Check for general LSB system
        if os.path.isfile(LSB_RELEASE):
            try:
                fields = dict((a.split('=') for a in rfile(LSB_RELEASE).split('\n') if len(a.split('=')) == 2))
                system_info['distname'] = fields['DISTRIB_ID']
                system_info['distver'] = fields['DISTRIB_RELEASE']
            except ValueError:
                pass
            except KeyError:
                pass
    return system_info


# Identified ranges

SEC = 1000
MIN = 60 * SEC
HOUR = 60 * MIN
DAY = 24 * HOUR
MON = 31 * DAY
YEAR = 365 * DAY


def date_patterns():
    """ Generates date patterns of the form [day<->month year?].
    """
    for year in [' %Y', ' %y']:
        for mon in ['%b', '%B', '%m']:
            yield ['%%d %s%s' % (mon, year), DAY, []]
            yield ['%s %%d%s' % (mon, year), DAY, []]
    for mon in ['%b', '%B']:  # Year empty
        yield ['%%d %s' % (mon), DAY, [YEAR]]
        yield ['%s %%d' % (mon), DAY, [YEAR]]
    yield ['%%Y %%d %s' % (mon), DAY, []]
    yield ['%%Y %s %%d' % (mon), DAY, []]
    yield ['%Y %m %d', DAY, []]


def time_patterns(c_cols):
    """Generates time patterns of the form [hour:min:sec?] including empty
    time.
    """
    if c_cols >= 2:
        yield ['%H:%M:%S', SEC, []]
    if c_cols >= 1:
        yield ['%H:%M', MIN, []]
        yield ['%I:%M%p', MIN, []]
    yield ['%I%p', HOUR, []]


def datetime_patterns(c_cols):
    """Generates combinations of date and time patterns.
    """
    # Generate dates only
    for date_pattern in date_patterns():
        yield date_pattern

    # Generate combinations
    for t in time_patterns(c_cols):
        for d in date_patterns():
            yield ['%s %s' % (d[0], t[0]), t[1], d[2]]
            yield ['%s %s' % (t[0], d[0]), t[1], d[2]]
        yield [t[0], t[1], [YEAR, MON, DAY]]


def timestamp_patterns(sample):
    """Generates all timestamp patterns we can handle. It is constructed by
    generating all possible combinations of date, time, day name and zone. The
    pattern is [day_name? date<->time zone?] plus simple date and time.
    """
    # All timestamps variations
    day_name = ''
    if len(sample) > 0:
        if sample[0] in string.ascii_letters:
            day_name = '%a '
    c_cols = sample.count(':')
    for zone in ['', ' %Z', ' %z']:
        for dt in datetime_patterns(c_cols):
            yield ['%s%s%s' % (day_name, dt[0], zone), dt[1], dt[2]]


def timestamp_group(text):
    """Returns a tuple [timestamp, range] which corresponds to the date and
    time given. Exists on parse error.
    """
    timep = re.sub(r' +', ' ', re.sub(r'[-,./]', ' ', text)).strip()
    start_tuple = None
    for p in timestamp_patterns(timep):
        pattern, resolution, filling = p
        try:
            start_tuple = time.strptime(timep, p[0])
            break
        except ValueError:
            pass
    if not start_tuple:
        die("Error: Date '%s' not recognized" % text)

    today = datetime.date.today()
    # Complete filling
    if YEAR in filling:
        start_tuple.rm_year = today.year
    if MON in filling:
        start_tuple.rm_month = today.month
    if DAY in filling:
        start_tuple.rm_day = today.day
    return [int(time.mktime(start_tuple)) * 1000, resolution]


def timestamp_range(text):
    """Identifies range in the text given. Returns -1 if the range has not been
    identified.  """

    # Parse range
    m = re.match(r'^(last)?\s*(\d+)?\s*(s|sec|second|m|min|minute|h|hour|d|day|mon|month|y|year)s?$', text.strip())
    if not m:
        return -1
    count = m.group(2)  # Count of time frames
    tf = m.group(3)  # Time frame
    # Get count
    if count:
        count = int(count)
    else:
        count = 1
    # Get time frame
    f_groups = [
        [['s', 'sec', 'second'], SEC],
        [['m', 'min', 'minute'], MIN],
        [['h', 'hour'], HOUR],
        [['d', 'day'], DAY],
        [['mon', 'month'], MON],
        [['y', 'year'], YEAR],
    ]
    for tg in f_groups:
        if tf in tg[0]:
            return count * tg[1]
    return -1


def parse_timestamp_range(text):
    """Parses the time range given and return start-end pair of timestamps.

    Recognized structures are:
    t|today
    y|yesterday
    last? \\d* (m|min|minute|h|hour|d|day|mon|month|y|year) s?
    range
    datetime
    datetime -> range
    datetime -> datetime
    """

    text = text.strip()
    # No time frame
    if text == '':
        return [0, 9223372036854775807]

    # Day spec
    now = datetime.datetime.now()
    if text in ['t', 'today']:
        today = int(time.mktime(datetime.datetime(now.year, now.month, now.day).timetuple())) * 1000
        return [today, today + DAY]
    if text in ['y', 'yesterday']:
        yesterday = int(time.mktime(
            (datetime.datetime(now.year, now.month, now.day) -
            datetime.timedelta(days=1)).timetuple())) * 1000
        return [yesterday, yesterday + DAY]

    # Range spec
    parts = text.split('->')
    r = timestamp_range(parts[0])
    if (r != -1 and len(parts) > 1) or len(parts) > 2:
        die("Error: Date and range '%s' has invalid structure" % text)
    if r != -1:
        now = int(time.time() * 1000)
        return [now - r, now]

    # Date spec
    start_group = timestamp_group(parts[0])
    start = start_group[0]
    end = start + start_group[1]

    if len(parts) > 1:
        end_range = timestamp_range(parts[1])
        if end_range != -1:
            end = start + end_range
        else:
            end_group = timestamp_group(parts[1])
            end = end_group[0] + end_group[1]

    return [start, end]


def choose_account_key(accounts):
    """
    Allows user to select the right account.
    """
    if len(accounts) == 0:
        die('No account is associated with your profile. Log in to Logentries to create a new account.')
    if len(accounts) == 1:
        return accounts[0]['account_key']

    for i in range(0, len(accounts)):
        account = accounts[i]
        print >> sys.stderr, '[%s] %s %s' % (
            i, account['account_key'][:8], account['name'])

    while True:
        try:
            selection = int(raw_input('Pick account you would like to use: '))
            if selection in range(0, len(accounts)):
                return accounts[selection]['account_key']
        except ValueError:
            pass
        print >> sys.stderr, 'Invalid choice. Please try again or break with Ctrl+C.'


def retrieve_account_key():
    """
    Retrieves account keys from the web server.
    """
    while True:
        try:
            username = raw_input('Email: ')
            password = getpass.getpass()
            c = domain_connect(config, Domain.MAIN, Domain)
            c.request('POST', ACCOUNT_KEYS_API,
                      urllib.urlencode({'username': username, 'password': password}),
                      {
                          'Referer': 'https://logentries.com/login/',
                          'Content-type': 'application/x-www-form-urlencoded',
                      })
            response = c.getresponse()
            if not response or response.status != 200:
                resp_val = 'err'
                if response:
                    resp_val = response.status
                if resp_val == 403:
                    print >> sys.stderr, 'Error: Login failed. Invalid credentials.'
                else:
                    print >> sys.stderr, 'Error: Unexpected login response from logentries (%s).' % resp_val
            else:
                data = json_loads(response.read())
                return choose_account_key(data['accounts'])
        except socket.error, msg:
            print >> sys.stderr, 'Error: Cannot contact server, %s' % msg
        except ValueError, msg:
            print >> sys.stderr, 'Error: Invalid response from the server (Parsing error %s)' % msg
        except KeyError:
            print >> sys.stderr, 'Error: Invalid response from the server, user key not present.'
        except EOFError:
            # Ctrl+D in get_pass, simulate Ctrl+C
            raise KeyboardInterrupt()

        print >> sys.stderr, 'Try to log in again, or press Ctrl+C to break'

class FollowMultilog(object):
    """
    The FollowMultilog is responsible for handling those logs that were set-up using the
    '--multilog' option and that may have a wildcard in the pathname.
    In which case multiple local (log) files will be followed, but with all the new events
    from all the files forwarded to the same single log in the logentries infrastructure.
    """
    def __init__(self,
                 name,
                 entry_filter,
                 entry_formatter,
                 entry_identifier,
                 transport,
                 states,
                 max_num_followers=MAX_FILES_FOLLOWED ):
        """ Initializes the FollowMultilog. """
        self.name = name
        self.flush = True
        self.entry_filter = entry_filter
        self.entry_formatter = entry_formatter
        self.entry_identifier = entry_identifier
        self.transport = transport

        self._states = states
        self._shutdown = False
        self._max_num_followers=max_num_followers
        self._followers = []
        self._worker = threading.Thread(
            target=self.supervise_followers, name=self.name)
        self._worker.daemon = True
        self._worker.start()

    def _file_test(self, candidate):
        """
        Only regular files passed
        """
        # Fail if a symbolic link
        if os.path.islink(candidate):
            return False
        # Fail if not a regular file (passes links!)
        if not os.path.isfile(candidate):
            return False
        return True

    def _append_followers(self, add_files, states={}):
        for filename in add_files:
            if len(self._followers) < self._max_num_followers:
                follower = Follower(filename,
                                    self.entry_filter,
                                    self.entry_formatter,
                                    self.entry_identifier,
                                    self.transport,
                                    states.get(filename),
                                    True)
                self._followers.append(follower)
                if config.debug_multilog:
                    print >> sys.stderr, "Number of followers increased to: %s" %len(self._followers)
            else:
                log.debug("Warning: Allowed maximum of files that can be followed reached")
                break

    def _remove_followers(self, removed_files):
        for follower in self._followers:
            if follower.name in removed_files:
                follower.close()
                self._followers.remove(follower)
                if config.debug_multilog:
                    print >> sys.stderr, "Number of followers decreased to: %s" %len(self._followers)

    def close(self):
        """
        Stops all FollowMultilog activity, and then loops through list of existing
        followers to close each one - then waits for the worker thread to stop.
        """
        self._shutdown = True
        # Run through list of followers closing each one
        for follower in self._followers:
            follower.close()
        self._worker.join(FOLLOWMULTI_JOIN_INTERVAL)

    def supervise_followers(self):
        """
         Instantiates a Follower object for each file found - all log events from all
         files are forwarded to the same log in the lE infrastructure
        """
        try:
            start_set = set([filename for filename in glob.glob(self.name)])
        except os.error:
            log.error("Error: FollowerMultiple glob has failed")
        if len(start_set) == 0:
            log.error("FollowMultilog: no files found in OS to be followed")
        else:
            self._append_followers(start_set, self._states)
        while not self._shutdown:
            time.sleep(RETRY_GLOB_INTERVAL)
            try:
                current_set = set([filename for filename in glob.glob(self.name)])
            except os.error:
                log.error("FollowerMultiple glob has failed")
            followed_files = [follower.name for follower in self._followers]
            added_files = [filename for filename in current_set if not filename in followed_files]
            self._append_followers(added_files)
            removed_files = [filename for filename in followed_files if not filename in current_set]
            self._remove_followers(removed_files)


class Follower(object):

    """
    The follower keeps an eye on the file specified and sends new events to the
    logentries infrastructure.  """

    def __init__(self,
                 name,
                 entry_filter,
                 entry_formatter,
                 entry_identifier,
                 transport,
                 state,
                 disable_glob=False):
        """ Initializes the follower. """
        self.name = name
        self.entry_filter = entry_filter
        self.entry_formatter = entry_formatter
        self.entry_identifier = entry_identifier
        self.transport = transport
        # FollowMultilog usage
        self._disable_glob = disable_glob

        self._load_state(state)
        self._file = None
        self._shutdown = False
        self._read_file_rest = ''
        self._entry_rest = []
        self._worker = threading.Thread(
            target=self.monitorlogs, name=self.name)
        self._worker.daemon = True
        self._worker.start()

    def get_state(self):
        return self._state

    def get_name(self):
        return self.name

    def _load_state(self, state):
        if state:
            self._update_state(state['filename'], state['position'])
        else:
            # -1 here means we'll seek to the end of the first file
            self._update_state(None, -1)

    def _update_state(self, real_name, file_position):
        self._state = {
            'filename': real_name,
            'position': file_position,
        }

    def _file_candidate(self):
        """
        Returns list of file names which corresponds to the specified template.
        """
        try:
            candidates = glob.glob(self.name)

            if len(candidates) == 0:
                return None

            candidate_times = [[os.path.getmtime(name), name]
                               for name in candidates]
            candidate_times.sort()
            candidate_times.reverse()
            return candidate_times[0][1]
        except os.error:
            return None

    def _open_log(self, filename=None, position=0):
        """Keeps trying to re-open the log file. Returns when the file has been
        opened or when requested to remove.

        filename, if specified, is name of a file that is being open on first attempt
        position indicates the desired initial position, -1 means end of file
        """
        error_info = True
        self.real_name = None
        first_try = True

        while not self._shutdown:
            # FollowMultilog usage
            if self._disable_glob:
                candidate = self.name
            else:
                if first_try and filename:
                    candidate = filename
                else:
                    candidate = self._file_candidate()

            if candidate:
                self.real_name = candidate
                try:
                    self._close_log()
                    self._file = open(self.real_name)
                    new_position = 0
                    if first_try:
                        if position == -1:
                            self._set_file_position(0, FILE_END)
                            new_position = self._get_file_position()
                        elif position != 0:
                            self._set_file_position(position)
                            new_position = position
                    self._update_state(self.real_name, new_position)
                    break
                except IOError:
                    pass

            if error_info:
                log.info("Cannot open file '%s', re-trying in %ss intervals",
                         self.name, REOPEN_INT)
                error_info = False
            first_try = False
            time.sleep(REOPEN_TRY_INTERVAL)

    def _close_log(self):
        if self._file:
            try:
                self._file.close()
            except IOError:
                pass
            self._file = None

    def _log_rename(self):
        """Detects file rename."""

        # Get file candidates
        candidate = self._file_candidate()
        if not candidate:
            return False

        try:
            ctime1 = os.fstat(self._file.fileno()).st_mtime
            ctime_new = os.path.getmtime(candidate)
            ctime2 = os.fstat(self._file.fileno()).st_mtime
        except os.error:
            pass

        if ctime1 == ctime2 and ctime1 != ctime_new:
            # We have a name change according to the time
            return True

        return False

    def _read_log_lines(self):
        """ Reads a block of lines from the log. Checks maximal line size. """
        buff = self._file.read(MAX_BLOCK_SIZE - len(self._read_file_rest))
        buff_lines = buff.split('\n')
        if len(self._read_file_rest) > 0:
            buff_lines[0] = self._read_file_rest + buff_lines[0]

        self._read_file_rest = buff_lines[-1]

        # Limit size of _read_file_rest
        if len(self._read_file_rest) >= MAX_BLOCK_SIZE:
            buff_lines.append(self._read_file_rest[:MAX_BLOCK_SIZE])
            self._read_file_rest = self._read_file_rest[MAX_BLOCK_SIZE:]

        return [line.decode('utf-8', 'ignore') for line in buff_lines[:-1]]

    def _set_file_position(self, offset, start=FILE_BEGIN):
        """ Move the position of filepointers."""
        self._file.seek(offset, start)

    def _get_file_position(self):
        """ Returns the position filepointers."""
        pos = self._file.tell()
        return pos

    def _collect_lines(self, lines):
        """Accepts lines received and merges them to multiline events.
        """
        # Fast track
        if not self.entry_identifier:
            return lines
        if not lines:
            if self._entry_rest:
                x = [LINE_SEPARATOR.join(self._entry_rest)]
                self._entry_rest = []
            else:
                x = []
            return x
        # Entry separator is specified
        new_lines = []
        new_entry = self._entry_rest
        self._entry_rest = []
        for line in lines:
            if self.entry_identifier.search(line):
                if new_entry:
                    new_lines.append(LINE_SEPARATOR.join(new_entry))
                    new_entry = []
                new_entry.append(line)
            else:
                new_entry.append(line)
        self._entry_rest = new_entry
        return new_lines

    def _get_lines(self):
        """Returns a block of newly detected line from the log. Returns None in
        case of timeout.
        """

        # TODO: investigate select-like approach?
        idle_cnt = 0
        lines = []
        while not self._shutdown:
            # Collect lines
            lines = self._read_log_lines()
            lines = self._collect_lines(lines)
            if lines:
                break

            # No line, wait
            time.sleep(TAIL_RECHECK)

            lines = self._collect_lines([])
            if lines:
                break

            # Log rename check
            idle_cnt += 1
            if idle_cnt == NAME_CHECK:
                if self._log_rename():
                    self._open_log()
                else:
                    # Recover from external file modification
                    position = self._get_file_position()
                    self._set_file_position(0, FILE_END)
                    file_size = self._get_file_position()

                    if file_size < position:
                        # File has been externaly modified
                        position = 0
                    self._set_file_position(position)
                idle_cnt = 0
            else:
                # To reset end-of-line error
                self._set_file_position(self._get_file_position())

        self._update_state(self.real_name, self._get_file_position())
        return lines

    def _send_lines(self, lines):
        """ Sends lines. """
        for line in lines:
            if not line:
                continue
            line = self.entry_filter(line)
            if not line:
                continue
            if config.debug_events:
                print >> sys.stderr, line
            line = self.entry_formatter(line)
            if not line:
                continue
            self.transport.send(line)

    def close(self):
        """Closes the follower by setting the shutdown flag and waiting for the
        worker thread to stop."""
        self._shutdown = True
        self._worker.join(FOLLOWER_JOIN_INTERVAL)

    def monitorlogs(self):
        """ Opens the log file and starts to collect new events. """
        # If there is a predefined state, try to load it up
        state = self.get_state()
        self._open_log(state['filename'], state['position'])
        while not self._shutdown:
            try:
                lines = self._get_lines()
                try:
                    self._send_lines(lines)
                except IOError, e:
                    if config.debug:
                        log.debug("IOError: %s", e)
                    self._open_log()
                except UnicodeError, e:
                    log.warn("UnicodeError sending lines `%s'", lines, exc_info=True)
                except Exception, e:
                    log.error("Caught unknown error `%s' while sending lines %s", e, lines, exc_info=True)
            except Exception, e:
                log.error("Caught unknown error `%s' while sending line", e, exc_info=True)
        if self._file:
            self._update_state(self.real_name, self._get_file_position())
        self._close_log()


class Transport(object):

    """Encapsulates simple connection to a remote host. The connection may be
    encrypted. Each communication is started with the preamble."""

    def __init__(self, endpoint, port, use_ssl, preamble, debug_transport_events, proxy):
        # Copy transport configuration
        self.endpoint = endpoint
        self.port = port
        self.use_ssl = use_ssl
        self.preamble = preamble
        self._entries = Queue.Queue(SEND_QUEUE_SIZE)
        self._socket = None # Socket with optional TLS encyption
        self._debug_transport_events = debug_transport_events

        self._shutdown = False # Shutdown flag - terminates the networking thread

        # proxy setup
        self._use_proxy = False

        (proxy_type_str, self._proxy_url, self._proxy_port) = proxy

        if proxy_type_str != NOT_SET and self._proxy_url != NOT_SET and self._proxy_port != NOT_SET:
            self._use_proxy = True
            if proxy_type_str == "HTTP":
                self._proxy_type = socks.PROXY_TYPE_HTTP
            elif proxy_type_str == "SOCKS5":
                self._proxy_type = socks.PROXY_TYPE_SOCKS5
            elif proxy_type_str == "SOCKS4":
                self._proxy_type = socks.PROXY_TYPE_SOCKS4
            else:
                self._use_proxy = False
                log.error("Invalide proxy type. Only HTTP, SOCKS5 and SOCKS4 are accepted")

        if self._use_proxy:
            log.info("Using proxy with proxy_type: %s, proxy-url: %s, proxy-port: %s",
                     proxy_type_str, self._proxy_url, self._proxy_port)

        # Get certificate name
        cert_name = None
        if not config.use_ca_provided:
            cert_name = system_cert_file()
            if cert_name is None:
                cert_name = default_cert_file(config)
        else:
            cert_name = default_cert_file(config)

        if use_ssl and not cert_name:
            die('Cannot get default certificate file name to provide connection over SSL!')
            # XXX Do we need to die here?
        self._certs = cert_name

        # Start asynchronous worker
        self._worker = threading.Thread(target=self.run)
        self._worker.daemon = True
        self._worker.start()

    def _get_address(self, use_proxy):
        if use_proxy:
            return self.endpoint
        else:
            """Returns an IP address of the endpoint. If the endpoint resolves to
            multiple addresses, a random one is selected. This works better than
            default selection."""
            return random.choice(
                socket.getaddrinfo(self.endpoint, self.port))[4][0]

    def _connect_ssl(self, plain_socket):
        """Connects the socket and wraps in SSL. Returns the wrapped socket
        or None in case of IO or other errors."""
        # FIXME this code ignores --local
        try:
            address = '-'
            address = self._get_address(self._use_proxy)
            s = plain_socket
            s.connect((address, self.port))

            if FEAT_SSL:
                try:
                    s = wrap_socket(
                        plain_socket, ca_certs=self._certs,
                        cert_reqs=ssl.CERT_REQUIRED, ssl_version=ssl.PROTOCOL_TLSv1,
                        ciphers="HIGH:-aNULL:-eNULL:-PSK:RC4-SHA:RC4-MD5")
                except TypeError:
                    s = wrap_socket(
                        plain_socket, ca_certs=self._certs, cert_reqs=ssl.CERT_REQUIRED,
                        ssl_version=ssl.PROTOCOL_TLSv1)

                try:
                    match_hostname(s.getpeercert(), self.endpoint)
                except CertificateError, ce:
                    report("Could not validate SSL certificate for %s: %s" %
                        (self.endpoint, ce.message))
                    return None
            else:
                s = wrap_socket(plain_socket, ca_certs=self._certs)
            return s

        except IOError, e:
            cause = e.strerror
            if not cause:
                cause = "(No reason given)"
            report("Can't connect to %s/%s via SSL at port %s. Make sure that the host and port are reachable "
                   "and speak SSL: %s" % (self.endpoint, address, self.port, cause))
        return None

    def _connect_plain(self, plain_socket):
        """Connects the socket with the socket given. Returns the socket or None in case of IO errors."""
        address = self._get_address(self._use_proxy)
        try:
            plain_socket.connect((address, self.port))
        except IOError, e:
            cause = e.strerror
            if not cause:
                cause = ""
            report("Can't connect to %s/%s at port %s. Make sure that the host and port are reachable\n"
                   "Error message: %s" % (self.endpoint, address, self.port, e.strerror))
            return None
        return plain_socket

    def _open_connection(self):
        """ Opens a push connection to logentries. """
        preamble = self.preamble.strip()
        if preamble:
            preamble = ' ' + preamble
        log.debug("Opening connection %s:%s%s",
                  self.endpoint, self.port, preamble)
        retry = 0
        delay = SRV_RECON_TO_MIN
        # Keep trying to open the connection
        while not self._shutdown:
            self._close_connection()
            try:
                s = None
                if self._use_proxy:
                    s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
                    s.setproxy(self._proxy_type, self._proxy_url, self._proxy_port)
                else:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                s.settimeout(TCP_TIMEOUT)
                if self.use_ssl:
                    self._socket = self._connect_ssl(s)
                else:
                    self._socket = self._connect_plain(s)

                # If the socket is open, send preamble and leave
                if self._socket:
                    if self.preamble:
                        self._socket.send(self.preamble)
                    break
            except socket.error:
                if self._shutdown:
                    return  # XXX

            # Wait between attempts
            time.sleep(delay)
            retry += 1
            delay *= 2
            if delay > SRV_RECON_TO_MAX:
                delay = SRV_RECON_TO_MAX

    def _close_connection(self):
        if self._socket:
            try:
                self._socket.close()
            except AttributeError:
                pass
            except socket.error:
                pass
            self._socket = None

    def _send_entry(self, entry):
        """Sends the entry. If the connection fails it will re-open it and try
        again."""
        # Keep sending data until successful
        while not self._shutdown:
            try:
                self._socket.send(entry.encode('utf8'))
                if self._debug_transport_events:
                    print >> sys.stderr, entry.encode('utf8'),
                break
            except socket.error:
                self._open_connection()

    def send(self, entry):
        """Sends the entry given. Depending on transport configuration it will
        block until the entry is sent or it will queue the entry for async
        send.

        Note: entry must end with a new line
        """
        while True:
            try:
                self._entries.put_nowait(entry)
                break
            except Queue.Full:
                try:
                    self._entries.get_nowait()
                except Queue.Empty:
                    pass

    def close(self):
        self._shutdown = True
        self.send('') # Force the networking thread to check the shutdown flag
        self._worker.join(TRANSPORT_JOIN_INTERVAL)

    def run(self):
        """When run with backgroud thread it collects entries from internal
        queue and sends them to destination."""
        self._open_connection()
        while not self._shutdown:
            try:
                try:
                    entry = self._entries.get(True, IAA_INTERVAL)
                except Queue.Empty:
                    entry = IAA_TOKEN
                self._send_entry(entry + '\n')
            except Exception:
                log.error("Exception in run: %s", traceback.format_exc())
        self._close_connection()


class DefaultTransport(object):

    def __init__(self, xconfig):
        self._transport = None
        self._config = xconfig

    def get(self):
        if not self._transport:
            use_ssl = not self._config.suppress_ssl
            if self._config.datahub:
                endpoint = self._config.datahub_ip
                port = self._config.datahub_port
            else:
                endpoint = Domain.DATA
                if use_ssl:
                    port = 443
                else:
                    port = 80
            if config.force_domain:
                endpoint = self._config.force_domain
            elif self._config.force_data_host:
                endpoint = self._config.force_data_host
            if self._config.debug_local:
                endpoint = Domain.LOCAL
                port = 10000
                use_ssl = False
            self._transport = Transport(
                endpoint, port, use_ssl, '', self._config.debug_transport_events,
                (self._config.proxy_type, self._config.proxy_url, self._config.proxy_port))
        return self._transport

    def close(self):
        if self._transport:
            self._transport.close()


class ConfiguredLog(object):

    def __init__(self, name, token, destination, path, formatter, entry_identifier):
        self.name = name
        self.token = token
        self.destination = destination
        self.path = path
        self.formatter = formatter
        self.entry_identifier = entry_identifier
        self.logset = None
        self.set_key = None
        self.log_key = None

    def is_logset(self):
        """
        Flag on whether its a valid sharedlog/logset.
        """
        return self.logset


class FatalConfigurationError(Exception):

    def __init__(self, msg):
        self.msg = msg


class Config(object):

    def __init__(self):
        self.config_dir_name = self.get_config_dir()
        self.config_filename = self.config_dir_name + LE_CONFIG
        self.config_d = os.path.join(self.config_dir_name, 'conf.d')
        self.include = NOT_SET

        # Configuration variables
        self.agent_key = NOT_SET
        self.suppress_ssl = False
        self.use_ca_provided = False
        self.user_key = DEFAULT_USER_KEY
        self.datahub = NOT_SET
        self.datahub_ip = NOT_SET
        self.datahub_port = NOT_SET
        self.system_stats_token = NOT_SET
        self.pull_server_side_config = NOT_SET
        self.configured_logs = []
        self.metrics = metrics.MetricsConfig()

        # Special options
        self.daemon = False
        self.filters = NOT_SET
        self.formatters = NOT_SET
        self.formatter = NOT_SET
        self.entry_identifier = NOT_SET
        self.force = False
        self.hostname = NOT_SET
        self.name = NOT_SET
        self.no_timestamps = False
        self.pid_file = PID_FILE
        self.std = False
        self.std_all = False
        self.system_stats_token = NOT_SET
        self.type_opt = NOT_SET
        self.uuid = False
        self.xlist = False
        self.yes = False
        self.multilog = False
        self.state_file = NOT_SET
        # Behaviour associated with daemontools/multilog

        #proxy
        self.use_proxy = NOT_SET
        self.proxy_type = NOT_SET
        self.proxy_url = NOT_SET
        self.proxy_port = NOT_SET

        # Debug options

        # Enabled fine-grained logging
        self.debug = False
        # Command line args to stderr
        self.debug_cmd_line = False
        # Multilog specific debugging to stderr
        self.debug_multilog = False
        # All recognized events are logged
        self.debug_events = False
        # All transported events are logged
        self.debug_transport_events = False
        # All filtering actions are logged
        self.debug_filters = False
        # All formattering actions are logged
        self.debug_formatters = False
        # All metrics actions are logged
        self.debug_metrics = False
        # Adapter connects to locahost
        self.debug_local = False
        # Do not collect statistics
        self.debug_nostats = False
        # Collected statistics are logged
        self.debug_stats = False
        # Collect statistics only
        self.debug_stats_only = False
        # Commands passed to server are logged
        self.debug_requests = False
        # Display system information and exit
        self.debug_system = False
        # Display list of logs in the system
        self.debug_loglist = False
        # Force host for api
        self.force_api_host = NOT_SET
        # Force host for data
        self.force_data_host = NOT_SET
        # Force host for this domain
        self.force_domain = NOT_SET

    def get_config_dir(self):
        """
        Identifies a configuration directory for the current user.
        Always terminated with slash.
        """
        if os.geteuid() == 0:
            # Running as root
            c_dir = CONFIG_DIR_SYSTEM
        else:
            # Running as an ordinary user
            c_dir = os.path.expanduser('~') + '/' + CONFIG_DIR_USER

        return c_dir + '/'

    def clean(self):
        """
        Wipes out old configuration file. Returns True if successful.
        """
        try:
            os.remove(self.config_filename)
        except OSError, e:
            if e.errno != 2:
                log.warning("Error: %s: %s",
                            self.config_filename, e.strerror)
                return False
        return True

    def _list_configs(self, path):
        """
        Returns a list of configuration files located in the path.
        """
        configs = []
        for root, _, files in os.walk(path):
            for filename in files:
                if filename.endswith(CONF_SUFFIX):
                    configs.append(os.path.join(root, filename))
        return sorted(configs)

    def _get_if_def(self, conf, param, param_name):
        if param == NOT_SET:
            new_param = conf.get(MAIN_SECT, param_name)
            if new_param != '':
                return new_param
        return param

    def load(self, load_include_dirs=True):
        """
        Initializes configuration parameters from the configuration
        file.  Returns True if successful, False otherwise. Does not
        touch already defined parameters.

        Args:
          load_include_dirs (bool): specify if files from the include
                                    directory are loaded
        """

        try:
            conf = ConfigParser.SafeConfigParser({
                USER_KEY_PARAM: '',
                AGENT_KEY_PARAM: '',
                FILTERS_PARAM: '',
                FORMATTERS_PARAM: '',
                FORMATTER_PARAM: '',
                ENTRY_IDENTIFIER_PARAM: '',
                SUPPRESS_SSL_PARAM: '',
                FORCE_DOMAIN_PARAM: '',
                USE_CA_PROVIDED_PARAM: '',
                DATAHUB_PARAM: '',
                SYSSTAT_TOKEN_PARAM: '',
                STATE_FILE_PARAM: '',
                HOSTNAME_PARAM: '',
                PULL_SERVER_SIDE_CONFIG_PARAM: 'True',
                INCLUDE_PARAM: '',
                PROXY_TYPE_PARAM: '',
                PROXY_URL_PARAM: '',
                PROXY_PORT_PARAM: '',
            })

            # Read configuration files from default directories
            config_files = [self.config_filename]
            if load_include_dirs:
                config_files.extend(self._list_configs(self.config_d))

            # Adjust configuration file permissions to be only readable by onwer + group
            for _config in config_files:
                try:
                    if not os.path.exists(_config):
                        continue

                    world_readable = bool(os.stat(_config).st_mode & stat.S_IROTH)
                    if world_readable:
                        os.chmod(_config, 0640)
                except OSError:
                    log.warn('Could not adjust permissions for config file %s', _config, exc_info=True)

            conf.read(config_files)

            # Fail if no configuration file exist
            if not conf.has_section(MAIN_SECT):
                return False

            # Get optional user-provided configuration directory
            self.include = self._get_if_def(conf, self.include, INCLUDE_PARAM)

            # Load configuration files from user-provided directory
            if load_include_dirs and self.include:
                config_files.extend(conf.read(self._list_configs(self.include)))

            log.debug('Configuration files loaded: %s', ', '.join(config_files))

            # Load parameters
            self.user_key = self._get_if_def(conf, self.user_key, USER_KEY_PARAM)
            self.agent_key = self._get_if_def(conf, self.agent_key, AGENT_KEY_PARAM)
            self.filters = self._get_if_def(conf, self.filters, FILTERS_PARAM)
            self.formatters = self._get_if_def(conf, self.formatters, FORMATTERS_PARAM)
            self.formatter = self._get_if_def(conf, self.formatter, FORMATTER_PARAM)
            self.entry_identifier = self._get_if_def(conf, self.entry_identifier, ENTRY_IDENTIFIER_PARAM)
            self.hostname = self._get_if_def(conf, self.hostname, HOSTNAME_PARAM)
            if self.pull_server_side_config == NOT_SET:
                new_pull_server_side_config = conf.get(MAIN_SECT, PULL_SERVER_SIDE_CONFIG_PARAM)
                self.pull_server_side_config = new_pull_server_side_config == 'True'
                if new_pull_server_side_config is None:
                    self.pull_server_side_config = True

            # Proxy configuration
            if self.proxy_type == NOT_SET:
                self.proxy_type = conf.get(MAIN_SECT, PROXY_TYPE_PARAM)
                if not self.proxy_type:
                    self.proxy_type = NOT_SET
            if self.proxy_url == NOT_SET:
                self.proxy_url = conf.get(MAIN_SECT, PROXY_URL_PARAM)
                if not self.proxy_url:
                    self.proxy_url = NOT_SET
            if self.proxy_port == NOT_SET:
                proxy_port = conf.get(MAIN_SECT, PROXY_PORT_PARAM)
                if not proxy_port:
                    self.proxy_port = NOT_SET
                else:
                    self.proxy_port = int(proxy_port)

            if self.proxy_type != NOT_SET and self.proxy_url != NOT_SET and self.proxy_port != NOT_SET:
                self.use_proxy = True
            else:
                self.use_proxy = False

            new_suppress_ssl = conf.get(MAIN_SECT, SUPPRESS_SSL_PARAM)
            if new_suppress_ssl == 'True':
                self.suppress_ssl = new_suppress_ssl == 'True'
            new_force_domain = conf.get(MAIN_SECT, FORCE_DOMAIN_PARAM)
            if new_force_domain:
                self.force_domain = new_force_domain
            if self.datahub == NOT_SET:
                self.set_datahub_settings(
                    conf.get(MAIN_SECT, DATAHUB_PARAM), should_die=False)
            if self.system_stats_token == NOT_SET:
                system_stats_token_str = conf.get(
                    MAIN_SECT, SYSSTAT_TOKEN_PARAM)
                if system_stats_token_str != '':
                    self.system_stats_token = system_stats_token_str
            if self.state_file == NOT_SET:
                state_file_str = conf.get(MAIN_SECT, STATE_FILE_PARAM)
                if state_file_str:
                    self.state_file = state_file_str

            self.metrics.load(conf)

            self.load_configured_logs(conf)

        except ConfigParser.NoSectionError, e0:
            raise FatalConfigurationError('%s'%e0)
        except ConfigParser.NoOptionError, e1:
            raise FatalConfigurationError('%s'%e1)
        except ConfigParser.MissingSectionHeaderError, e2:
            raise FatalConfigurationError('%s'%e2)
        return True

    def load_configured_logs(self, conf):
        global log
        """
        Loads configured logs from the configuration file.
        These are logs that use tokens.
        """
        self.configured_logs = []
        account_hosts = None
        for name in conf.sections():
            if name != MAIN_SECT:
                token = ''
                try:
                    xtoken = conf.get(name, TOKEN_PARAM)
                    if xtoken:
                        token = uuid_parse(xtoken)
                        if not token:
                            log.warning("Invalid log token `%s' in application `%s'.", xtoken, name)
                except ConfigParser.NoOptionError:
                    pass

                try:
                    path = conf.get(name, PATH_PARAM)
                except ConfigParser.NoOptionError:
                    log.debug("Not following logs for application `%s' as `%s' parameter is not specified", name, PATH_PARAM)
                    continue

                destination = ''
                try:
                    destination = conf.get(name, DESTINATION_PARAM)
                except ConfigParser.NoOptionError:
                    pass

                formatter = ''
                try:
                    formatter = conf.get(name, FORMATTER_PARAM)
                except ConfigParser.NoOptionError:
                    pass

                entry_identifier = ''
                try:
                    entry_identifier = conf.get(name, ENTRY_IDENTIFIER_PARAM)
                except ConfigParser.NoOptionError:
                    pass

                configured_log = ConfiguredLog(name, token, destination, path, formatter, entry_identifier)
                self.configured_logs.append(configured_log)

    def save(self):
        """
        Saves configuration parameters into the configuration file.
        The file with certificates is added as well.
        """
        try:
            conf = ConfigParser.SafeConfigParser()
            create_conf_dir(self)
            conf_file = open(self.config_filename, 'wb')
            conf.add_section(MAIN_SECT)
            if self.user_key != NOT_SET:
                conf.set(MAIN_SECT, USER_KEY_PARAM, self.user_key)
            if self.agent_key != NOT_SET:
                conf.set(MAIN_SECT, AGENT_KEY_PARAM, self.agent_key)
            if self.filters != NOT_SET:
                conf.set(MAIN_SECT, FILTERS_PARAM, self.filters)
            if self.formatters != NOT_SET:
                conf.set(MAIN_SECT, FORMATTERS_PARAM, self.formatters)
            if self.formatter != NOT_SET:
                conf.set(MAIN_SECT, FORMATTER_PARAM, self.formatter)
            if self.hostname != NOT_SET:
                conf.set(MAIN_SECT, HOSTNAME_PARAM, self.hostname)
            if self.suppress_ssl:
                conf.set(MAIN_SECT, SUPPRESS_SSL_PARAM, 'True')
            if self.use_ca_provided:
                conf.set(MAIN_SECT, USE_CA_PROVIDED_PARAM, 'True')
            if self.force_domain:
                conf.set(MAIN_SECT, FORCE_DOMAIN_PARAM, self.force_domain)
            if self.pull_server_side_config != NOT_SET:
                conf.set(MAIN_SECT, PULL_SERVER_SIDE_CONFIG_PARAM, "%s" %
                         self.pull_server_side_config)
            if self.datahub != NOT_SET:
                conf.set(MAIN_SECT, DATAHUB_PARAM, self.datahub)
            if self.system_stats_token != NOT_SET:
                conf.set(
                    MAIN_SECT, SYSSTAT_TOKEN_PARAM, self.system_stats_token)

            for clog in self.configured_logs:
                conf.add_section(clog.name)
                if clog.token:
                    conf.set(clog.name, TOKEN_PARAM, clog.token)
                conf.set(clog.name, PATH_PARAM, clog.path)
                if clog.destination:
                    conf.set(clog.name, DESTINATION_PARAM, clog.destination)

            self.metrics.save(conf)

            conf.write(conf_file)
        except IOError, e:
            die("Error: IO error when writing to config file: %s" % e)

    def check_key(self, key):
        """
        Checks if the key looks fine
        """
        return len(key) == KEY_LEN

    def set_user_key(self, value):
        if not self.check_key(value):
            die('Error: User key does not look right.')
        self.user_key = value

    def user_key_required(self, ask_for_it):
        """
        Exits with error message if the user key is not defined.
        """
        if self.user_key == NOT_SET:
            if ask_for_it:
                log.info(
                    "Account key is required. Enter your Logentries login "
                    "credentials or specify the account key with "
                    "--account-key parameter.")
                self.user_key = retrieve_account_key()
            else:
                die("Account key is required. Enter your account key with --account-key parameter.")
            config.save()

    def set_system_stat_token(self, value):
        if not self.check_key(value):
            die('Error: system stat token does not look right.')
        self.system_stats_token = value

    def system_stats_token_required(self):
        if self.system_stats_token == NOT_SET:
            die("System stat token is required.")
        config.save()

    def set_agent_key(self, value):
        if not self.check_key(value):
            die('Error: Agent key does not look right.')
        self.agent_key = value

    def agent_key_required(self):
        """
        Exits with error message if the agent key is not defined.
        """
        if self.agent_key == NOT_SET:
            die("Host key is required. Register the host or specify the host key with the --host-key parameter.")

    def have_agent_key(self):
        """Tests if the agent key has been assigned to this instance."""
        return self.agent_key != ''

    def hostname_required(self):
        """
        Sets the hostname parameter based on server network name. If
        the hostname is set already, it is kept untouched.
        """
        if self.hostname == NOT_SET:
            self.hostname = socket.getfqdn()
        return self.hostname

    def name_required(self):
        """
        Sets host name if not set already. The new host name is
        delivered from its hostname. As a side effect this
        function sets a hostname as well.
        """
        if self.name == NOT_SET:
            self.name = self.hostname_required().split('.')[0]
        return self.name

    # The method gets all parameters of given type from argument list,
    # checks for their format and returns list of values of parameters
    # of specified type. E.g: We have params = ['true', 127.0.0.1, 10000] the call of
    # check_and_get_param_by_type(params, type='bool') yields [True]

    @staticmethod
    def check_and_get_param_by_type(params, type='bool'):
        ret_param = []

        for p in params:
            found = False
            p = p.lower()
            if type == 'ipaddr':
                if p.find('.') != -1:
                    octets = p.split('.', 4)
                    octets_ok = True
                    if len(octets) == 4:
                        for octet in octets:
                            octets_ok &= (octet.isdigit()) and (0 <= int(octet) <= 255)
                    else:
                        octets_ok = False
                    found = octets_ok
            elif type == 'bool':
                if (p.find('true') != -1 and len(p) == 4) or (p.find('false') != -1 and len(p) == 5):
                    found = True
            elif type == 'numeric':
                if p.isdigit():
                    found = True
            else:
                raise NameError('Unknown type name')

            if found:
                if type == 'numeric':
                    ret_param.append(int(p))
                elif type == 'bool':
                    ret_param.append(p == 'true')
                else:
                    ret_param.append(p)

        return ret_param

    def set_datahub_settings(self, value, should_die=True):
        if not value and should_die:
            die('--datahub requires a parameter')
        elif not value and not should_die:
            return

        values = value.split(":")
        if len(values) > 2:
            die("Cannot parse %s for --datahub. Expected format: hostname:port" %
                value)

        self.datahub_ip = values[0]
        if len(values) == 2:
            try:
                self.datahub_port = int(values[1])
            except ValueError:
                die("Cannot parse %s as port. Specify a valid --datahub address" %
                    values[1])
        self.datahub = value

    def validate_pathname(self, args=None, cmd_line=True, path=None):
        """
        For the '--multilog' option where a wildcard can be used in the directory name.
        Validates the string that is passed to the agent from command line, config file or server.
        If error from command line, then error message written to commond line and agent quits.
        If error from config file (or server) then error message written to log and False is returned.
        :param args: the pathname given to the agent
        :return:    True if okay, the agent will die otherwise
        """
        if cmd_line and path is None:
            if args is not None:
                pname_slice = args[1:]
                # Validate that a pathname is detected in parameters to agent
                if len(pname_slice) == 0:
                    die("Error: No pathname detected - Specify the path to the file to be followed\n" + MULTILOG_USAGE, EXIT_OK)
                # Validate that agent is not receiving a list of pathnames (possibly shell is expanding wildcard)
                if len(pname_slice) > 1:
                    die("Error: Too many arguments being passed to agent\n" + MULTILOG_USAGE, EXIT_OK)
                pname = str(pname_slice[0])
        elif not cmd_line and path is None:
            # For anything not coming in on command line no output is written to command line
            log.error("Error: Pathname argument is empty")
            return False
        elif not cmd_line and path is not None:
            pname=path
        filename = os.path.basename(pname)
        # Verify there is a filename
        if not filename:
            if not cmd_line:
                log.error("Error: No filename detected in the pathname")
                return False
            else:
                die("Error: No filename detected - Specify the filename to be followed\n" + MULTILOG_USAGE, EXIT_OK)
        # Check if a wildcard detected in pathname
        if '*' in pname:
            # Verify that only one wildcard is in pathname
            if pname.count('*') > 1:
                if not cmd_line:
                    log.error("Error: More then one wildcard * detected in pathname")
                    return False
                else:
                    die("Error: Only one wildcard * allowed\n" + MULTILOG_USAGE, EXIT_OK)
            # Verify that no wildcard is in filename
            if '*' in filename:
                if not cmd_line:
                    log.error("Error: Wildcard detected in filename of path argument")
                    return False
                else:
                    die("Error: No wildcard * allowed in filename\n" + MULTILOG_USAGE, EXIT_OK)
        return True

    def process_params(self, params):
        """
        Parses command line parameters and updates config parameters accordingly
        """
        param_list = """user-key= account-key= agent-key= host-key= no-timestamps debug-events
                    debug-transport-events debug-metrics
                    debug-filters debug-formatters debug-loglist local debug-stats debug-nostats
                    debug-stats-only debug-cmd-line debug-system help version yes force id uuid list
                    std std-all name= hostname= type= pid-file= debug no-defaults
                    suppress-ssl use-ca-provided force-api-host= force-domain=
                    system-stat-token= datahub=
                    pull-server-side-config= config= config.d= multilog debug-multilog"""
        try:
            optlist, args = getopt.gnu_getopt(params, '', param_list.split())
        except getopt.GetoptError, err:
            die("Parameter error: " + str(err))
        for name, value in optlist:
            if name == "--help":
                print_usage()
            if name == "--version":
                print_usage(True)
            if name == "--config":
                self.config_filename = value
            if name == "--config.d":
                self.config_d = value
            if name == "--yes":
                self.yes = True
            elif name == "--user-key":
                self.set_user_key(value)
            elif name == "--account-key":
                self.set_user_key(value)
            elif name == "--agent-key":
                self.set_agent_key(value)
            elif name == "--host-key":
                self.set_agent_key(value)
            elif name == "--force":
                self.force = True
            elif name == "--list":
                self.xlist = True
            elif name == "--id":
                self.uuid = True
            elif name == "--uuid":
                self.uuid = True
            elif name == "--name":
                self.name = value
            elif name == "--hostname":
                self.hostname = value
            elif name == "--pid-file":
                if value == '':
                    self.pid_file = None
                else:
                    self.pid_file = value
            elif name == "--std":
                self.std = True
            elif name == "--type":
                self.type_opt = value
            elif name == "--std-all":
                self.std_all = True
            elif name == "--no-timestamps":
                self.no_timestamps = True
            elif name == "--debug":
                self.debug = True
            elif name == "--debug-cmd-line":
                self.debug_cmd_line = True
            elif name == "--debug-multilog":
                self.debug_multilog = True
            elif name == "--debug-events":
                self.debug_events = True
            elif name == "--debug-transport-events":
                self.debug_transport_events = True
            elif name == "--debug-filters":
                self.debug_filters = True
            elif name == "--debug-formatters":
                self.debug_formatters = True
            elif name == "--debug-metrics":
                self.debug_metrics = True
            elif name == "--local":
                self.debug_local = True
            elif name == "--debug-stats":
                self.debug_stats = True
            elif name == "--debug-nostats":
                self.debug_nostats = True
            elif name == "--debug-stats-only":
                self.debug_stats_only = True
            elif name == "--debug-loglist":
                self.debug_loglist = True
            elif name == "--debug-requests":
                self.debug_requests = True
            elif name == "--debug-system":
                self.debug_system = True
            elif name == "--suppress-ssl":
                self.suppress_ssl = True
            elif name == "--force-api-host":
                if value and value != '':
                    self.force_api_host = value
            elif name == "--force-data-host":
                if value and value != '':
                    self.force_data_host = value
            elif name == "--force-domain":
                if value and value != '':
                    self.force_domain = value
            elif name == "--use-ca-provided":
                self.use_ca_provided = True
            elif name == "--system-stat-token":
                self.set_system_stat_token(value)
            elif name == "--pull-server-side-config":
                self.pull_server_side_config = value == "True"
            elif name == "--datahub":
                self.set_datahub_settings(value)
            elif name == "--multilog":
                # self.multilog is only True if pathname is good
                self.multilog = self.validate_pathname(args,True,None)

        if self.datahub_ip and not self.datahub_port:
            if self.suppress_ssl:
                self.datahub_port = LE_DEFAULT_NON_SSL_PORT
            else:
                self.datahub_port = LE_DEFAULT_SSL_PORT

        if self.debug_local and self.force_api_host:
            die("Do not specify --local and --force-api-host at the same time.")
        if self.debug_local and self.force_data_host:
            die("Do not specify --local and --force-data-host at the same time.")
        if self.debug_local and self.force_domain:
            die("Do not specify --local and --force-domain at the same time.")
        return args

config = Config()


def do_request(conn, operation, addr, data=None, headers={}):
    log.debug('Domain request: %s %s %s %s', operation, addr, data, headers)
    if data:
        conn.request(operation, addr, data, headers=headers)
    else:
        conn.request(operation, addr, headers=headers)


def get_response(operation, addr, data=None, headers={}, silent=False, die_on_error=True, domain=Domain.API):
    """
    Returns response from the domain or API server.
    """
    response = None
    conn = None
    try:
        conn = domain_connect(config, domain, Domain)
        do_request(conn, operation, addr, data, headers)
        response = conn.getresponse()
        return response, conn
    except socket.sslerror, msg:  # Network error
        if not silent:
            log.info("SSL error: %s", msg)
    except socket.error, msg:  # Network error
        if not silent:
            log.debug("Network error: %s", msg)
    except httplib.BadStatusLine:
        error = "Internal error, bad status line"
        if die_on_error:
            die(error)
        else:
            log.info(error)

    return None, None


def api_request(request, required=False, check_status=False, silent=False, die_on_error=True):
    """
    Processes a request on the logentries domain.
    """
    # Obtain response
    request_encoded = urllib.urlencode(request)
    response, conn = get_response(
        "POST", LE_SERVER_API, request_encoded,
        silent=silent, die_on_error=die_on_error, domain=Domain.API,
        headers={'Content-Type': 'application/x-www-form-urlencoded'})

    # Check the response
    if not response:
        if required:
            error("Cannot process LE request, no response")
        if conn:
            conn.close()
        return None
    if response.status != 200:
        if required:
            error("Cannot process LE request: (%s)", response.status)
        conn.close()
        return None

    xresponse = response.read()
    conn.close()
    log.debug('Domain response: "%s"', xresponse)
    try:
        d_response = json_loads(xresponse)
    except ValueError:
        error = 'Error: Invalid response, parse error.'
        if die_on_error:
            die(error)
        else:
            log.info(error)
            d_response = None

    if check_status and d_response['response'] != 'ok':
        reason = d_response['reason']

        # Special compatibility case: change group to host
        reason = reason.replace( 'The group with ID', 'The host with ID')

        error = "Error: %s" % reason
        if die_on_error:
            die(error)
        else:
            log.info(error)
            d_response = None

    return d_response



def api_v2_request(method, url, request, required=False, silent=False, die_on_error=True):
    """
    Processes a request on the logentries domain.
    """
    # Obtain response
    request_encoded = json.dumps(request)
    response, conn = get_response(
        method, '/v2/accounts/%s/%s'%(config.user_key, url), request_encoded,
        silent=silent, die_on_error=die_on_error, domain=Domain.API,
        headers={'Content-Type': 'application/x-www-form-urlencoded'})

    # Check the response
    if not response:
        if required:
            error("Cannot process LE request, no response")
        if conn:
            conn.close()
        return None

    xresponse = response.read()
    conn.close()

    log.debug('Domain response: "%s"', xresponse)
    try:
        if xresponse:
            d_response = json_loads(xresponse)
        else:
            d_response = {}
    except ValueError:
        error = 'Error: Invalid response, parse error.'
        if die_on_error:
            die(error)
        else:
            log.info(error)
            d_response = None

    if response.status not in [httplib.OK, httplib.CREATED, httplib.NO_CONTENT]:
        reason = ''
        if 'reason' in d_response:
            reason = d_response['reason']
        if required:
            if reason:
                error("%s" % reason)
            else:
                error("Cannot process LE request: (%s)", response.status)
        return None

    return d_response


def pull_request(what, params):
    """
    Processes a pull request on the logentries domain.
    """
    response = None

    # Obtain response
    addr = '/%s/%s/?%s' % (
        config.user_key, urllib.quote(what), urllib.urlencode(params))
    response, conn = get_response("GET", addr, domain=Domain.PULL)

    # Check the response
    if not response:
        error("Cannot process LE request, no response")
    if response.status == 404:
        error("Log not found")
    if response.status != 200:
        error("Cannot process LE request: (%s)", response.status)

    while True:
        data = response.read(65536)
        if len(data) == 0:
            break
        sys.stdout.write(data)
    conn.close()


def request(request, required=False, check_status=False, rtype='GET', retry=False):
    """
    Processes a list request on the API server.
    """
    noticed = False
    while True:
        # Obtain response
        response, conn = get_response(
            rtype, urllib.quote('/' + config.user_key + '/' + request),
            die_on_error=not retry)

        # Check the response
        if response:
            break
        if required:
            error('Cannot process LE request, no response')
        if retry:
            if not noticed:
                log.info('Error: No response from LE, re-trying in %ss intervals',
                         SRV_RECON_TIMEOUT)
                noticed = True
            time.sleep(SRV_RECON_TIMEOUT)
        else:
            return None

    response = response.read()
    conn.close()
    log.debug('List response: %s', response)
    try:
        d_response = json_loads(response)
    except ValueError:
        error('Invalid response (%s)', response)

    if check_status and d_response['response'] != 'ok':
        error('%s', '%s' % d_response['reason'])

    return d_response


def _startup_info():
    """
    Prints correct startup information based on OS
    """
    if 'darwin' in sys.platform:
        log.info(
            '  sudo launchctl unload /Library/LaunchDaemons/com.logentries.agent.plist')
        log.info(
            '  sudo launchctl load /Library/LaunchDaemons/com.logentries.agent.plist')
    elif 'linux' in sys.platform:
        log.info('  sudo service logentries restart')
    elif 'sunos' in sys.platform:
        log.info('  sudo svcadm disable logentries')
        log.info('  sudo svcadm enable logentries')
    else:
        log.info('')


def create_log(host_key, name, filename, type_opt, do_follow=True, source=None):
    """
    Creates a log on server with given parameters.
    """
    request = {
        'request': 'new_log',
        'user_key': config.user_key,
        'host_key': host_key,
        'name': name,
        'filename': filename,
        'type': type_opt,
    }
    request['follow'] = 'true'

    if not do_follow:
        request['follow'] = 'false'

    if source:
        request['source'] = source
    resp = api_request(request, True, True)

    if resp['response'] == 'ok':
        return resp['log']
    return None


def create_host(name, hostname, system, distname, distver):
    """
    Creates a new host on server with given parameters.
    """
    request = {
        'request': 'register',
        'user_key': config.user_key,
        'name': name,
        'hostname': hostname,
        'system': system,
        'distname': distname,
        'distver': distver
    }
    resp = api_request(request, True, True)
    if resp['response'] == 'ok':
        return resp['host']
    else:
        return None


def request_follow(filename, name, type_opt):
    """
    Creates a new log to follow the file given.
    """
    config.agent_key_required()
    followed_log = create_log(config.agent_key, name, filename, type_opt)
    print "Will follow %s as %s" % (filename, name)
    log.info("Don't forget to restart the daemon")
    _startup_info()
    return followed_log


def request_hosts(load_logs=False):
    """Returns list of registered hosts.
    """
    if load_logs:
        xload_logs = 'true'
    else:
        xload_logs = 'false'
    response = api_request({
        'request': 'get_user',
        'load_hosts': 'true',
        'load_logs': xload_logs,
        'user_key': config.user_key}, True, True)

    return response['hosts']


def get_or_create_host(host_name):
    """Gets or creates a new host.
    """
    # Retrieve the host via API
    account_hosts = request_hosts(load_logs=True)
    host = find_api_obj_by_name(account_hosts, host_name)

    if not host:
        # If it does not exist, create a new one
        host = create_host(host_name, '', '', '', '')

    return host['key']


def get_or_create_log(host_key, log_name, destination):
    """ Gets or creates a log for the host given. It returns logs's token or
    None.
    """
    if not host_key:
        return None

    # Retrieve the log via API
    account_hosts = request_hosts(load_logs=True)
    host = find_api_obj_by_key(account_hosts, host_key)
    if not host:
        return None
    xlog = find_api_obj_by_name(host['logs'], log_name)
    if not xlog:
        # Try to create the log
        xlog = create_log(host['key'], log_name, '', '', do_follow=False, source='token')
        if not xlog:
            return None

    return xlog.get('token', None)


#
# Commands
#

def cmd_init(args):
    """
    Saves variables given to the configuration file. Variables not
    specified are not saved and thus are overwritten with default value.
    The configuration directory is created if it does not exit.
    """
    no_more_args(args)
    config.user_key_required(True)
    config.save()
    log.info("Initialized")


def cmd_reinit(args):
    """
    Saves variables given to the configuration file. The configuration
    directory is created if it does not exit.
    """
    no_more_args(args)
    config.load(load_include_dirs=False)
    config.save()
    log.info("Reinitialized")


def cmd_register(args):
    """
    Registers the agent in logentries infrastructure. The newly obtained
    agent key is stored in the configuration file.
    """
    no_more_args(args)
    config.load()

    if config.agent_key != NOT_SET and not config.force:
        report("Warning: Server already registered. Use --force to override current registration.")
        return
    config.user_key_required(True)
    config.hostname_required()
    config.name_required()

    si = system_detect(True)

    host = create_host(config.name, config.hostname, si['system'], si['distname'], si['distver'])

    config.agent_key = host['key']
    config.save()

    log.info("Registered %s (%s)", config.name, config.hostname)

    # Registering logs
    logs = []
    if config.std or config.std_all:
        logs = collect_log_names(si)
    for logx in logs:
        if config.std_all or logx['default'] == '1':
            request_follow(logx['filename'], logx['name'], logx['type'])

# The function checks for 2 things: 1) that the path is not empty;
# 2) the path starts with '/' character which indicates that the log has
# a "physical" path which starts from filesystem root.


def check_file_name(file_name):
    return file_name.startswith('/')


def get_filters(available_filters, filter_filenames, log_name, log_id, log_filename, log_token):
    # Check filters
    if not filter_filenames(log_filename):
        debug_filters(
            " Log blocked by filter_filenames, not following")
        log.info(
            'Not following %s, blocked by filter_filenames', log_name)
        return None
    debug_filters(
        " Looking for filters by log_name=%s log_id=%s token=%s", log_name, log_id, log_token)

    entry_filter = None
    if not entry_filter and log_name:
        debug_filters(" Looking for filters by log name")
        entry_filter = available_filters.get(log_name)
        if not entry_filter:
            debug_filters(" No filter found by log name")

    if not entry_filter and log_id:
        debug_filters(" Looking for filters by log ID")
        entry_filter = available_filters.get(log_id)
        if not entry_filter:
            debug_filters(" No filter found by log ID")

    if not entry_filter and log_token:
        debug_filters(" Looking for filters by token")
        entry_filter = available_filters.get(log_token)
        if not entry_filter:
            debug_filters(" No filter found by token")

    if entry_filter and not hasattr(entry_filter, '__call__'):
        debug_filters(
            " Filter found, but ignored because it's not a function")
        entry_filter = None
    if not entry_filter:
        entry_filter = filter_events
        debug_filters(" No filter found")
    else:
        debug_filters(" Using filter %s", entry_filter)
    return entry_filter


def get_formatters(default_formatter, available_formatters, log_name, log_id, log_filename, log_token):
    debug_formatters(
        " Looking for formatters by log_name=%s id=%s token=%s", log_name, log_id, log_token)

    entry_formatter = None
    if not entry_formatter and log_name:
        debug_formatters(" Looking for formatters by log name")
        entry_formatter = available_formatters.get(log_name)
        if not entry_formatter:
            debug_formatters(" No formatter found by log name")

    if not entry_formatter and log_id:
        debug_formatters(" Looking for formatters by log ID")
        entry_formatter = available_formatters.get(log_id)
        if not entry_formatter:
            debug_formatters(" No formatter found by log ID")

    if not entry_formatter and log_token:
        debug_formatters(" Looking for formatters by token")
        entry_formatter = available_formatters.get(log_token)
        if not entry_formatter:
            debug_formatters(" No formatter found by token")

    if entry_formatter and not hasattr(entry_formatter, '__call__'):
        debug_formatters(
            " Formatter found, but ignored because it's not a function")
        entry_formatter = None

    if entry_formatter:
        form = entry_formatter(config.hostname, log_name, log_token)
        debug_formatters(" Formatter found")
    else:
        form = default_formatter
        debug_formatters(" No formatter found")

    return form

def _init_entry_identifier(entry_identifier):
    """Compiles entry separator defined by regular expression. If the
    compilation is not successfull, it return None.
    """
    try:
        return re.compile(entry_identifier)
    except re.error:
        return None

def start_followers(default_transport, states, terminate):
    """
    Loads logs from the server (or configuration) and initializes followers.
    """
    noticed = False
    logs = []
    followers = []
    transports = []
    follow_multilogs = []

    if config.pull_server_side_config:
        # Use LE server as the source for list of followed logs
        server_logs = []
        while not server_logs and not terminate.terminate:
            resp = request('hosts/%s/' %
                           config.agent_key, False, False, retry=True)
            if resp['response'] != 'ok':
                if not noticed:
                    log.error('Error retrieving list of logs: %s, retrying in %ss intervals',
                              resp['reason'], SRV_RECON_TIMEOUT)
                    noticed = True
                time.sleep(SRV_RECON_TIMEOUT)
                continue
            server_logs = resp['list']
            if not server_logs:
                time.sleep(SRV_RECON_TIMEOUT)
        # Select logs for the agent
        for l in server_logs:
            if l.get('follow') == 'true':
                l['formatter'] = ''
                l['entry_identifier'] = ''
                logs.append(l)

    for cl in config.configured_logs:
        # Construct response-like item which has the same structure as ones
        # returned by LE Server.
        logs.append(
            {'type': 'token', 'name': cl.name, 'filename': cl.path, 'key': '', 'token': cl.token,
                     'formatter': cl.formatter, 'entry_identifier': cl.entry_identifier, 'follow': 'true'})

    available_filters = {}
    filter_filenames = default_filter_filenames
    if config.filters != NOT_SET:
        sys.path.append(config.filters)
        try:
            import filters

            available_filters = getattr(filters, 'filters', {})
            filter_filenames = getattr(
                filters, 'filter_filenames', default_filter_filenames)

            debug_filters("Available filters: %s", available_filters.keys())
            debug_filters("Filter filenames: %s", filter_filenames)
        except:
            log.error('Cannot import event filter module %s: %s',
                      config.filters, sys.exc_info()[1])
            log.error('Details: %s', traceback.print_exc(sys.exc_info()))

    available_formatters = {}
    if config.formatters != NOT_SET:
        sys.path.append(config.formatters)
        try:
            import formatters

            available_formatters = getattr(formatters, 'formatters', {})
            debug_formatters("Available formatters: %s", available_formatters.keys())
        except:
            log.error('Cannot import event formatter module %s: %s',
                      config.formatters, sys.exc_info()[1])
            log.error('Details: %s', traceback.print_exc(sys.exc_info()))

    # Start followers
    for l in logs:
        # Note! Token-type logs have follow param == false by default, so we need to
        # check also the type of the log.
        if l['follow'] == 'true' or l['type'] == 'token':
            log_name = l['name']
            log_filename = l['filename']
            log_key = l['key']
            log_token = ''
            if l['type'] == 'token':
                log_token = l['token']
            multilog_filename = False
            if log_filename.startswith(PREFIX_MULTILOG_FILENAME):
                log_filename = log_filename.replace(PREFIX_MULTILOG_FILENAME,'',1).lstrip()
                if not config.validate_pathname(None,False,log_filename):
                    continue
                multilog_filename = True

            # Do not start a follower for a log with absent filepath.
            if not check_file_name(log_filename):
                continue
            #log.info("After check_file_name:log_filename %s",log_filename )

            entry_filter = get_filters(available_filters, filter_filenames,
                                       log_name, log_key, log_filename,
                                       log_token)
            if not entry_filter:
                continue

            # Formatter is taken according to local specification, global specification
            # and user-provided formatter
            entry_formatter = formats.get_formatter(l['formatter'], config.hostname, log_name, log_token)
            if not entry_formatter:
                entry_formatter = formats.get_formatter(config.formatter, config.hostname, log_name, log_token)
            entry_formatter = get_formatters(entry_formatter, available_formatters,
                                             log_name, log_key, log_filename,
                                             log_token)

            s_entry_identifier = l['entry_identifier']
            if not s_entry_identifier:
                s_entry_identifier = config.entry_identifier
            if s_entry_identifier:
                entry_identifier = _init_entry_identifier(s_entry_identifier)
                if not entry_identifier:
                    log.error("Invalid entry separator `%s' ignored", s_entry_identifier)
            else:
                entry_identifier = None

            log.info("Following %s", log_filename)

            if log_token or config.datahub:
                transport = default_transport.get()
            elif log_key:
                endpoint = Domain.DATA
                port = 443
                use_ssl = not config.suppress_ssl
                if not use_ssl:
                    port = 80
                if config.force_domain:
                    endpoint = config.force_domain
                if config.debug_local:
                    endpoint = Domain.LOCAL
                    port = 8081
                    use_ssl = False
                preamble = 'PUT /%s/hosts/%s/%s/?realtime=1 HTTP/1.0\r\n\r\n' % (
                    config.user_key, config.agent_key, log_key)

                # Special case for HTTP PUT
                # Use plain formatter if no formatter is defined
                transport = Transport(endpoint, port, use_ssl, preamble, config.debug_transport_events,
                                      (config.proxy_type, config.proxy_url, config.proxy_port))
                transports.append(transport)
                # Default formatter is plain
                if not entry_formatter:
                    entry_formatter = formats.get_formatter('plain', config.hostname, log_name, log_token)
            else:
                continue

            # Default formatter is syslog
            if not entry_formatter:
                entry_formatter = formats.get_formatter('syslog', config.hostname, log_name, log_token)

            # Instantiate the follow_multilog for 'multilog' filename, otherwise the individual follower
            if multilog_filename:
                follow_multilog = FollowMultilog(log_filename, entry_filter, entry_formatter, entry_identifier, transport, states)
                follow_multilogs.append(follow_multilog)
            else:
                follower = Follower(log_filename, entry_filter, entry_formatter, entry_identifier, transport, states.get(log_filename))
                followers.append(follower)
    return (followers, transports, follow_multilogs)


def is_followed(filename):
    """Checks if the file given is followed.
    """
    host = request('hosts/%s/' % config.agent_key, True, True)
    logs = host['list']
    for ilog in logs:
        if ilog['follow'] == 'true' and filename == ilog['filename']:
            return True
    return False

def get_log_names_for_files(filenames):
    """
    Checks if each file in a list of files is followed. Will only make the one call on the server!
    If it is, gets the 'name' of the log for this file. If not, then a 'None' is used.
    :param filenames:   the list of filenames of interest
    :return:    returns a {} of filenames with either the
                associated log name or 'None' for each file
    """
    if len(filenames) == 0:
        die('\nWarning: List of filenames is empty\n')
    host = request('hosts/%s/' % config.agent_key, True, True)
    logs = host['list']
    result = {}
    for filename in filenames:
        result[filename] = NOT_SET
        for ilog in logs:
            if ilog['follow'] == 'true' and filename == ilog['filename']:
                result[filename] = str(ilog['name'])
    return result


def get_loglist_with_paths():
    """
        Returns a list of all destination logs on the logentries infrastructure for
        a host with the path that the log is using for following a file or mutliple files
    :return :
    """
    host = request('hosts/%s/' % config.agent_key, True, True)
    logs = host['list']
    result = {}
    for ilog in logs:
        if ilog['follow'] == 'true':
            result[str(ilog['name'])] = str(ilog['filename'])
    return result


def create_configured_logs(configured_logs):
    """ Get tokens for all configured logs. Logs with no token specified are
    retrieved via API and created if needed.
    """
    for clog in configured_logs:
        if not clog.destination and not clog.token:
            log.debug("Not following logs for application `%s' as neither `%s' nor `%s' parameter is specified", clog.name, TOKEN_PARAM, DESTINATION_PARAM)
            continue

        if clog.destination and not clog.token:
            try:
                (hostname, logname) = clog.destination.split('/', 1)
            except ValueError:
                log.error('Ignoring section %s since `%s\' does not contain host', clog.name, DESTINATION_PARAM)
            host_key = get_or_create_host(hostname)
            token = get_or_create_log(host_key, logname, clog.destination)
            if not token:
                log.error('Ignoring section %s, cannot create log' % clog.name)

            clog.token = token


def load_state(state_file):
    if state_file:
        try:
            stat_file = open(state_file, 'r')
            state_s = stat_file.read()
            stat_file.close()

            state = json.loads(state_s)
            for name in state:
                state[name]['filename']
                state[name]['position']

            return state
        except IOError:
            pass
        except ValueError:
            pass
        except KeyError:
            pass
    return {} # Fallback


def save_state(state_file, followers):
    if state_file:
        # Collect statees from all followers
        states = {}
        for follower in followers:
            states[ follower.get_name()] = follower.get_state()
        try:
            # Save statees in state file
            tmp_name = config.state_file + '.tmp'
            sfile = open(tmp_name, 'w')
            content = json_dumps(states, sort_keys=True, indent=2) + '\n'
            sfile.write(content)
            sfile.close()
            # Update the state file
            os.rename(tmp_name, config.state_file)
        except IOError:
            # Not too much we can do here
            pass


class TerminationNotifier(object):
    terminate = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.signal_callback)
        signal.signal(signal.SIGTERM, self.signal_callback)

    def signal_callback(self, signum, frame):
        self.terminate = True


def cmd_monitor(args):
    """Monitors host activity and sends events collected to logentries
    infrastructure.
    """
    no_more_args(args)
    config.load()
    stats = None
    smetrics = None

    # We need account and host ID to get server side configuration
    if config.pull_server_side_config:
        config.user_key_required(not config.daemon)
        config.agent_key_required()

    # Ensure all configured logs are created
    if config.configured_logs and not config.datahub:
        create_configured_logs(config.configured_logs)

    if config.daemon:
        daemonize()

    # Start default transport channel
    default_transport = DefaultTransport(config)

    formatter = formats.FormatSyslog(config.hostname, 'le',
                                     config.metrics.token)
    smetrics = metrics.Metrics(config.metrics, default_transport,
                                formatter, config.debug_metrics)
    smetrics.start()

    followers = []
    transports = []
    follow_multilogs = []
    terminate = TerminationNotifier()
    try:
        state = load_state(config.state_file)

        # Load logs to follow and start following them
        if not config.debug_stats_only:
            (followers, transports, follow_multilogs) = start_followers(default_transport, state, terminate)

        # Periodically save state
        while not terminate.terminate:
            save_state(config.state_file, followers)

            time.sleep(1)
    except KeyboardInterrupt:
        pass

    print >> sys.stderr, "\nShutting down"
    # Stop metrics
    if smetrics:
        smetrics.cancel()
    # Close followers
    for follower in followers:
        follower.close()
    # Close each follow_multilog and the followers it holds
    for follow_multilog in follow_multilogs:
        follow_multilog.close()
    # Close transports
    for transport in transports:
        transport.close()
    default_transport.close()
    # Collect statuses
    save_state(config.state_file, followers)


def cmd_monitor_daemon(args):
    """Monitors as a daemon host activity and sends events collected to
    logentries infrastructure.
    """
    config.daemon = True
    cmd_monitor(args)


def cmd_follow(args):
    """
    Follow the log file given.
    """
    if len(args) == 0:
        error("Specify the file name of the log to follow.")
    if len(args) > 1:
        die("Error: Too many arguments.\n"
            "A common mistake is to use wildcards in path that is being "
            "expanded by shell. Enclose the path in single quotes to avoid "
            "expansion.")

    config.load()
    config.agent_key_required()
    # FIXME: follow to add logs into local configuration

    arg = args[0]
    filename = os.path.abspath(arg)
    name = config.name
    if name == NOT_SET:
        name = os.path.basename(filename)
    type_opt = config.type_opt
    if type_opt == NOT_SET:
        type_opt = ""

    # Check that we don't follow that file already
    if not config.force and is_followed(filename):
        log.warning('Already following %s', filename)
        return

    if len(glob.glob(filename)) == 0:
        log.warning('\nWarning: File %s does not exist\n', filename)

    request_follow(filename, name, type_opt)


def cmd_follow_multilog(args):
    """
    Follow the log(s) as defined in string passed to agent with
    the '--multilog' parameter included - modification of cmd_follow
    """
    if len(args) == 0:
        error("Specify the file name of the log to follow.")
    if len(args) > 1:
        die("Error: Too many arguments.\n"
            "A common mistake is to use wildcards in path that is being "
            "expanded by shell. Enclose the path in single quotes to avoid "
            "expansion.")
    config.load()
    config.agent_key_required()
    arg = args[0]
    path = os.path.abspath(arg)
    # When testing ignore user input
    if config.debug_multilog:
        follow = True
    else:
        follow = user_prompt(path)
    if follow:
        name = config.name
        if name == NOT_SET:
            name = os.path.basename(path)
        type_opt = config.type_opt
        if type_opt == NOT_SET:
            type_opt = ""
        filename = PREFIX_MULTILOG_FILENAME + path
        request_follow(filename, name, type_opt)

def user_prompt(path):
    """
    Displays 2 lists - files already followed with log names, and those not.
    Prompts user if they wish to follow files or not
    """
    file_candidates = glob.glob(path)
    loglist_with_paths = get_loglist_with_paths()
    identical_path = False
    print "\nExisting destination Logs for this host and the associated Paths are:"
    print('\t{0:50}{1}'.format('LOGNAME', 'PATH'))
    for logname, filepath in loglist_with_paths.items():
        # Test if an identical path is already in use!
        if path == filepath.replace(PREFIX_MULTILOG_FILENAME,'',1).lstrip():
            identical_path = True
            print('\t{0:40}{1:10}{2}'.format(logname,"IDENTICAL", filepath))
        else:
            print('\t{0:50}{1}'.format(logname, filepath))
    if identical_path:
        print "NOTE: there are destination logs in above list with identical paths."
    print "\nRequested path is: %s" % path
    if len(file_candidates) == 0:
        print "\nNo Files were found for this path at this time.\n"
    else:
        print "\nFiles found for this path:"
        file_count = 0
        for filename in file_candidates:
            if file_count < MAX_FILES_FOLLOWED:
                print ('\t{0}'.format(filename))
                file_count = file_count+1
    while True:
        print "\nUse new path to follow files [y] or quit [n]?"
        user_resp = raw_input().lower()
        if user_resp == 'n':
            sys.exit(EXIT_OK)
        elif user_resp == 'y':
            return True
        else:
            print "Please try again"

def cmd_followed(args):
    """
    Check if the log file given is followed.
    """
    if len(args) == 0:
        error("Specify the file name of the log to test.")
    if len(args) != 1:
        error("Too many arguments. Only one file name allowed.")
    config.load()
    config.agent_key_required()

    filename = os.path.abspath(args[0])

    # Check that we don't follow that file already
    if is_followed(filename):
        print 'Following %s' % filename
        sys.exit(EXIT_OK)
    else:
        print 'NOT following %s' % filename
        sys.exit(EXIT_NO)


def cmd_clean(args):
    """
    Wipes out old configuration file.
    """
    no_more_args(args)
    if config.clean():
        log.info('Configuration clean')


def cmd_whoami(args):
    """
    Displays information about this host.
    """
    config.load()
    config.agent_key_required()
    no_more_args(args)

    list_object(request('hosts/%s' % config.agent_key, True, True))
    print ''
    list_object(request('hosts/%s/' % config.agent_key, True, True))


def logtype_name(logtype_uuid):
    """ Provides name for the logtype given.
    """
    # Look for embedded structures
    for structure_name, structure_id in EMBEDDED_STRUCTURES.iteritems():
        if structure_id == logtype_uuid:
            return structure_name

    # Search for logtypes provided by the backend
    response = request('logtypes', True, True)
    all_logtypes = response['list']
    for logtype in all_logtypes:
        if logtype_uuid == logtype['key']:
            return logtype['shortcut']

    return 'unknown'


def list_object(request, hostnames=False):
    """
    Lists object request given.
    """
    t = request['object']
    index_name = 'name'
    item_name = ''
    if t == 'rootlist':
        item_name = 'item'
    elif t == 'host':
        print 'name =', request['name']
        print 'hostname =', request['hostname']
        print 'key =', request['key']
        print 'distribution =', request['distname']
        print 'distver =', request['distver']
        return
    elif t == 'log':
        print 'name =', request['name']
        print 'filename =', request['filename']
        print 'key =', request['key']
        print 'type =', request['type']
        print 'follow =', request['follow']
        if 'token' in request:
            print 'token =', request['token']
        if 'logtype' in request:
            print 'logtype =', logtype_name(request['logtype'])
        return
    elif t == 'list':
        print 'name =', request['name']
        return
    elif t == 'hostlist':
        item_name = 'host'
        if hostnames:
            index_name = 'hostname'
    elif t == 'logtype':
        print 'title =', request['title']
        print 'description =', request['desc']
        print 'shortcut =', request['shortcut']
        return
    elif t == 'loglist':
        item_name = 'log'
    elif t == 'logtypelist':
        item_name = 'logtype'
        index_name = 'shortcut'
    else:
        die('Unknown object type "%s". Agent too old?' % t)

    # Standard list, print it sorted
    ilist = request['list']
    ilist = sorted(ilist, key=lambda item: item[index_name])
    for item in ilist:
        if config.uuid:
            print item['key'],
        print "%s" % (item[index_name])
    print_total(ilist, item_name)


def is_log_fs(addr):
    """Tests if the address points for a log.
    """
    log_addrs = [r'(logs|apps)/.*/',
                 r'host(name)?s/.*/.*/']
    for la in log_addrs:
        if re.match(la, addr):
            return True
    return False


def cmd_ls_ips():
    """
    List IPs used by the agent.
    """
    l = []
    for name in [Domain.MAIN, Domain.API, Domain.DATA, Domain.PULL]:
        for info in socket.getaddrinfo(name, None, 0, 0, socket.IPPROTO_TCP):
            ip = info[4][0]
            print >>sys.stderr, '%-16s %s' % (ip, name)
            l.append(ip)
    print l
    print ' '.join(l)


def cmd_ls_structures():
    """
    List user defined structures.
    """
    config.load()
    config.user_key_required(True)

    response = api_v2_request('GET', 'structures', {}, True)
    structures = response['structures']

    structures = response['structures']
    for structure in sorted(structures, key=lambda x: x['name']):
        if config.uuid:
            print c_id(structure['id']),
        print structure['name']

    if len(structures) == 0:
        print >> sys.stderr, 'No structures defined'
    elif len(structures) == 1:
        print >> sys.stderr, '1 structure'
    else:
        print >> sys.stderr, '%s structures' % len(structures)


def cmd_ls_patterns(structure_name):
    """
    Lists patterns associated with the structure given.
    """
    if not structure_name:
        error('Structure name not specified')

    config.load()
    config.user_key_required(True)

    response = api_v2_request('GET', 'structures', {}, True)
    structures = response['structures']

    # Find structure
    matches = [s['id'] for s in structures if structure_name.lower() == s['id'].lower() or structure_name == s['name']]
    if len(matches) == 0:
        error('Structure `%s\' does not exist', structure_name)
    if len(matches) > 1:
        error('Multiple matches for `%s\'', structure_name)
    structure_id = matches[0]

    response = api_v2_request('GET', 'structures/%s/patterns'%structure_id, {}, True)

    patterns = response['patterns']
    for pattern in sorted(patterns, cmp=cmp_patterns):
        if config.uuid:
            print c_id(pattern['id']),
        print '%2d %s' % (pattern['priority'], pattern['pattern'])
    if len(patterns) == 0:
        print >> sys.stderr, 'No patterns in structure `%s\'' % structure_name
    elif len(patterns) == 1:
        print >> sys.stderr, '1 pattern'
    else:
        print >> sys.stderr, '%s patterns' % len(patterns)


def cmd_ls(args):
    """
    General list command
    """
    if len(args) == 1 and args[0] == 'ips':
        cmd_ls_ips()
        return
    if len(args) == 1 and args[0] == 'structures':
        cmd_ls_structures()
        return
    if len(args) >= 1 and args[0].startswith('structures/'):
        if len(args) == 1:
            cmd_ls_patterns(args[0][len('structures/'):])
        else:
            die('Error: Too many arguments.')
        return
    if len(args) == 0:
        args = ['/']
    config.load()
    config.user_key_required(True)

    addr = args[0]
    if addr.startswith('/'):
        addr = addr[1:]
    # Make sure we are not downloading log
    if is_log_fs(addr):
        die('Use pull to get log content.')

    # if addr.count('/') > 2:
    # die( 'Path not found')
    list_object(request(addr, True, True),
                hostnames=addr.startswith('hostnames'))


def cmd_add_structure(args):
    """
    Add a new structure command.

    Args:
        args: structure name followed by (optionally) pattern and priority
    """
    if not args:
        error('No structure name specified')
    structure_name = args[0].strip()
    if not structure_name:
        error('Empty structure name')

    pattern = ''
    priority = -1

    # Get and check the pattern
    if len(args) > 1:
        pattern = args[1]
        if not pattern:
            error('Pattern in empty')

    if len(args) > 2:
        try:
            priority = int(args[2])
            if priority < 0:
                error('Priority must be positive')
            if priority > MAX_PATTERN_PRIORITY:
                error('Priority `%s\'is above the limit (%s)', args[2], MAX_PATTERN_PRIORITY)
        except ValueError:
            error('Invalid priority `%s\', must be a positive integer', args[2])

    if len(args) > 3:
        error('Too many arguments')

    config.load()
    config.user_key_required(True)

    # Get all structures
    response = api_v2_request('GET', 'structures', {}, True)
    structures = response['structures']

    # Find the structure
    matches = [s['id'] for s in structures if structure_name.lower() == s['id'].lower() or structure_name == s['name']]
    if len(matches) == 0:
        # Add the structure
        response = api_v2_request('POST', 'structures', {
            'name': structure_name,
            'shortcut': structure_name,
            'description': '',
            'aux': {},
            }, True)
        print >> sys.stderr, 'Added structure `%s\'' % structure_name
        structure_id = response['structure']['id']
    else:
        structure_id = matches[0]
        if not pattern:
            print >> sys.stderr, 'Structure `%s\' already exists' % structure_name

    # Add pattern (if specified)
    # TODO - check that the pattern does not exist already
    if pattern:
        response = api_v2_request('POST', 'structures/%s/patterns'%structure_id, {
            'priority': priority,
            'pattern': pattern,
            }, True)
        print >> sys.stderr, 'Added pattern `%s\'' % pattern


def cmd_add(args):
    """
    General add command.
    """
    if len(args) >= 1 and args[0] == 'structure':
        cmd_add_structure(args[1:])
    elif len(args) >= 1 and args[0].startswith('structures/'):
        cmd_add_structure([args[0][len('structures/'):]] + args[1:])
    elif len(args) == 0:
        error('Specify what to add, i.e. structure')
    else:
        error('Unknown item to add: `%s\'', args[0])


def cmd_rm_pattern(patterns, structure_name, structure_id):
    if not patterns:
        error('No pattern specified (append pattern ID or beginning of the pattern or .) to remove.')
    if len(patterns) > 1:
        error('Too many arguments, only one pattern allowed')
    pattern = patterns[0]

    rm_all = pattern in ['*', '.']

    # Load all patterns
    response = api_v2_request('GET', 'structures/%s/patterns'%structure_id, {}, True)
    patterns = response['patterns']

    # Go though patterns one by one, identify pattern IDs
    # Use a different call for pattern=*
    matches = [[p['id'], p['pattern']] for p in patterns \
            if rm_all or p['id'] == pattern or p['pattern'].startswith(pattern)]
    if not matches:
        if rm_all:
            print >> sys.stderr, 'No pattern to be removed; structure is empty'
        else:
            error('No pattern matching `%s\' found', pattern)
    if len(matches) > 1 and not rm_all:
        error('Pattern `%s\' is not specific enough; multiple matches', pattern)

    # Do the physical deletion
    for pattern_id, pattern_p in matches:
        response = api_v2_request('DELETE', 'structures/%s/patterns/%s'%(structure_id, pattern_id), {}, True)
        print >> sys.stderr, 'Removed pattern `%s\'' % pattern_p


def cmd_rm_structure(args):
    """ Remove the structure (or pattern) command.

    Arguments contain command line (including 'structure' at the beginning)
    """
    subject = args[0]
    structure_name = ''
    if subject == 'structures':
        # We don't support removing structures
        error('Invalid command. Use `rm structure name\' or `rm structures/name\'')
    if subject == 'structure':
        if len(args) == 1:
            error('No structure name specified (append structure name)')
        if len(args) > 2:
            error('Too many structure names specified (specify only one name)')
        structure_name = args[1]
        patterns = args[2:]
    elif subject.startswith('structures/'):
        structure_name = subject[len('structures/'):]
        patterns = args[1:]

    if not structure_name:
        error('No structure name specified (append structure name)')

    # Note args contain structure name or ID, and an optional pattern

    config.load()
    config.user_key_required(True)

    # Load all structures
    response = api_v2_request('GET', 'structures', {}, True)
    structures = response['structures']

    # Find structure IDs
    structure = [[structure_name, s['id']] for s in structures if structure_name.lower() == s['id'].lower() or structure_name == s['name']]
    if not structure:
        error('Structure `%s\' does not exist', structure_name)
    if len(structure) > 1:
        error('Multiple matches for `%s\'', structure_name)
    structure_id = structure[0][1]

    # Now we know structure exists and we know its ID

    if not patterns: # Removing structure
        response = api_v2_request('DELETE', 'structures/%s'%structure_id, {}, True)
        print >> sys.stderr, 'Removed structure `%s\'' % structure_name
    else: # Removing patterns
        cmd_rm_pattern(patterns, structure_name, structure_id)


def cmd_rm(args):
    """
    General remove command
    """
    # In case of removing structures and patterns
    if args and (args[0] in ['structure', 'structures'] or args[0].startswith('structures/')):
        cmd_rm_structure(args)
        return

    if not args:
        args = ['/']

    config.load()
    config.user_key_required(True)

    addr = args[0]
    if addr.startswith('/'):
        addr = addr[1:]
    if addr.count('/') > 2:
        die('Path not found')
    response = request(addr, True, True, rtype='DELETE')
    report(response['reason'])


def cmd_pull(args):
    """
    Log pull command
    """
    if len(args) == 0:
        die(PULL_USAGE)
    config.load()
    config.user_key_required(True)

    params = {}

    addr = args[0]
    if addr.startswith('/'):
        addr = addr[1:]
    if addr.endswith('/'):
        addr = addr[:-1]
    if not is_log_fs(addr + '/'):
        die('Error: Not a log')

    if len(args) > 1:
        time_range = parse_timestamp_range(args[1])
        params['start'] = time_range[0]
        params['end'] = time_range[1]
    if len(args) > 2:
        params['filter'] = args[2]
    if len(args) > 3:
        try:
            limit = int(args[3])
        except ValueError:
            die('Error: Limit must be integer')
        if limit < 1:
            die('Limit must be above 0')
        params['limit'] = limit

    pull_request(addr, params)


#
# Main method
#

def main_root():
    """Serious business starts here.
    """
    # Read command line parameters
    args = config.process_params(sys.argv[1:])

    if config.debug:
        log.setLevel(logging.DEBUG)
    if config.debug_system:
        die(system_detect(True))
    if config.debug_loglist:
        die(collect_log_names(system_detect(True)))

    if config.debug_cmd_line:
        print >> sys.stderr, 'Debug command line args: %s' % args

    argv0 = sys.argv[0]
    if argv0 and argv0 != '':
        pname = os.path.basename(argv0).split('-')
        if len(pname) != 1:
            args.insert(0, pname[-1])

    if len(args) == 0:
        report(USAGE)
        sys.exit(EXIT_HELP)

    commands = {
        'init': cmd_init,
        'reinit': cmd_reinit,
        'register': cmd_register,
        'monitor': cmd_monitor,
        'monitordaemon': cmd_monitor_daemon,
        'follow': cmd_follow,
        'followed': cmd_followed,
        'clean': cmd_clean,
        'whoami': cmd_whoami,
        'add': cmd_add,
        # Filesystem operations
        'ls': cmd_ls,
        'list': cmd_ls,
        'rm': cmd_rm,
        'remove': cmd_rm,
        'pull': cmd_pull,
    }
    for cmd, func in commands.items():
        if cmd == args[0]:
            if config.multilog and cmd == 'follow':
                return cmd_follow_multilog(args[1:])
            else:
                return func(args[1:])
    error('Unknown command "%s".', args[0])


def main():
    try:
        main_root()
    except FatalConfigurationError, e:
        log.error("Fatal: %s", e.msg)
    except KeyboardInterrupt:
        die("\nTerminated", EXIT_TERMINATED)

if __name__ == '__main__':
    main()
