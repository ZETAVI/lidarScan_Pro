# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ydlidar
else:
    import _ydlidar

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _ydlidar.delete_SwigPyIterator

    def value(self):
        return _ydlidar.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _ydlidar.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _ydlidar.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _ydlidar.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _ydlidar.SwigPyIterator_equal(self, x)

    def copy(self):
        return _ydlidar.SwigPyIterator_copy(self)

    def next(self):
        return _ydlidar.SwigPyIterator_next(self)

    def __next__(self):
        return _ydlidar.SwigPyIterator___next__(self)

    def previous(self):
        return _ydlidar.SwigPyIterator_previous(self)

    def advance(self, n):
        return _ydlidar.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _ydlidar.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _ydlidar.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _ydlidar.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _ydlidar.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _ydlidar.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _ydlidar.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _ydlidar:
_ydlidar.SwigPyIterator_swigregister(SwigPyIterator)

class PointVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _ydlidar.PointVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _ydlidar.PointVector___nonzero__(self)

    def __bool__(self):
        return _ydlidar.PointVector___bool__(self)

    def __len__(self):
        return _ydlidar.PointVector___len__(self)

    def __getslice__(self, i, j):
        return _ydlidar.PointVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _ydlidar.PointVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _ydlidar.PointVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _ydlidar.PointVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _ydlidar.PointVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _ydlidar.PointVector___setitem__(self, *args)

    def pop(self):
        return _ydlidar.PointVector_pop(self)

    def append(self, x):
        return _ydlidar.PointVector_append(self, x)

    def empty(self):
        return _ydlidar.PointVector_empty(self)

    def size(self):
        return _ydlidar.PointVector_size(self)

    def swap(self, v):
        return _ydlidar.PointVector_swap(self, v)

    def begin(self):
        return _ydlidar.PointVector_begin(self)

    def end(self):
        return _ydlidar.PointVector_end(self)

    def rbegin(self):
        return _ydlidar.PointVector_rbegin(self)

    def rend(self):
        return _ydlidar.PointVector_rend(self)

    def clear(self):
        return _ydlidar.PointVector_clear(self)

    def get_allocator(self):
        return _ydlidar.PointVector_get_allocator(self)

    def pop_back(self):
        return _ydlidar.PointVector_pop_back(self)

    def erase(self, *args):
        return _ydlidar.PointVector_erase(self, *args)

    def __init__(self, *args):
        _ydlidar.PointVector_swiginit(self, _ydlidar.new_PointVector(*args))

    def push_back(self, x):
        return _ydlidar.PointVector_push_back(self, x)

    def front(self):
        return _ydlidar.PointVector_front(self)

    def back(self):
        return _ydlidar.PointVector_back(self)

    def assign(self, n, x):
        return _ydlidar.PointVector_assign(self, n, x)

    def resize(self, *args):
        return _ydlidar.PointVector_resize(self, *args)

    def insert(self, *args):
        return _ydlidar.PointVector_insert(self, *args)

    def reserve(self, n):
        return _ydlidar.PointVector_reserve(self, n)

    def capacity(self):
        return _ydlidar.PointVector_capacity(self)
    __swig_destroy__ = _ydlidar.delete_PointVector

# Register PointVector in _ydlidar:
_ydlidar.PointVector_swigregister(PointVector)

class Str2strMap(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _ydlidar.Str2strMap_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _ydlidar.Str2strMap___nonzero__(self)

    def __bool__(self):
        return _ydlidar.Str2strMap___bool__(self)

    def __len__(self):
        return _ydlidar.Str2strMap___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _ydlidar.Str2strMap___getitem__(self, key)

    def __delitem__(self, key):
        return _ydlidar.Str2strMap___delitem__(self, key)

    def has_key(self, key):
        return _ydlidar.Str2strMap_has_key(self, key)

    def keys(self):
        return _ydlidar.Str2strMap_keys(self)

    def values(self):
        return _ydlidar.Str2strMap_values(self)

    def items(self):
        return _ydlidar.Str2strMap_items(self)

    def __contains__(self, key):
        return _ydlidar.Str2strMap___contains__(self, key)

    def key_iterator(self):
        return _ydlidar.Str2strMap_key_iterator(self)

    def value_iterator(self):
        return _ydlidar.Str2strMap_value_iterator(self)

    def __setitem__(self, *args):
        return _ydlidar.Str2strMap___setitem__(self, *args)

    def asdict(self):
        return _ydlidar.Str2strMap_asdict(self)

    def __init__(self, *args):
        _ydlidar.Str2strMap_swiginit(self, _ydlidar.new_Str2strMap(*args))

    def empty(self):
        return _ydlidar.Str2strMap_empty(self)

    def size(self):
        return _ydlidar.Str2strMap_size(self)

    def swap(self, v):
        return _ydlidar.Str2strMap_swap(self, v)

    def begin(self):
        return _ydlidar.Str2strMap_begin(self)

    def end(self):
        return _ydlidar.Str2strMap_end(self)

    def rbegin(self):
        return _ydlidar.Str2strMap_rbegin(self)

    def rend(self):
        return _ydlidar.Str2strMap_rend(self)

    def clear(self):
        return _ydlidar.Str2strMap_clear(self)

    def get_allocator(self):
        return _ydlidar.Str2strMap_get_allocator(self)

    def count(self, x):
        return _ydlidar.Str2strMap_count(self, x)

    def erase(self, *args):
        return _ydlidar.Str2strMap_erase(self, *args)

    def find(self, x):
        return _ydlidar.Str2strMap_find(self, x)

    def lower_bound(self, x):
        return _ydlidar.Str2strMap_lower_bound(self, x)

    def upper_bound(self, x):
        return _ydlidar.Str2strMap_upper_bound(self, x)
    __swig_destroy__ = _ydlidar.delete_Str2strMap

# Register Str2strMap in _ydlidar:
_ydlidar.Str2strMap_swigregister(Str2strMap)

class CYdLidar(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _ydlidar.CYdLidar_swiginit(self, _ydlidar.new_CYdLidar())
    __swig_destroy__ = _ydlidar.delete_CYdLidar

    def initialize(self):
        return _ydlidar.CYdLidar_initialize(self)

    def GetLidarVersion(self, version):
        return _ydlidar.CYdLidar_GetLidarVersion(self, version)

    def turnOn(self):
        return _ydlidar.CYdLidar_turnOn(self)

    def doProcessSimple(self, outscan):
        return _ydlidar.CYdLidar_doProcessSimple(self, outscan)

    def turnOff(self):
        return _ydlidar.CYdLidar_turnOff(self)

    def disconnecting(self):
        return _ydlidar.CYdLidar_disconnecting(self)

    def DescribeError(self):
        return _ydlidar.CYdLidar_DescribeError(self)

    def setlidaropt(self, *args):
        return _ydlidar.CYdLidar_setlidaropt(self, *args)

    def getlidaropt_toInt(self, optname):
        return _ydlidar.CYdLidar_getlidaropt_toInt(self, optname)

    def getlidaropt_toBool(self, optname):
        return _ydlidar.CYdLidar_getlidaropt_toBool(self, optname)

    def getlidaropt_toFloat(self, optname):
        return _ydlidar.CYdLidar_getlidaropt_toFloat(self, optname)

    def getlidaropt_toString(self, optname):
        return _ydlidar.CYdLidar_getlidaropt_toString(self, optname)

# Register CYdLidar in _ydlidar:
_ydlidar.CYdLidar_swigregister(CYdLidar)


def os_init():
    return _ydlidar.os_init()

def os_isOk():
    return _ydlidar.os_isOk()

def os_shutdown():
    return _ydlidar.os_shutdown()

def lidarPortList():
    return _ydlidar.lidarPortList()
class LaserDebug(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    W3F4CusMajor_W4F0CusMinor = property(_ydlidar.LaserDebug_W3F4CusMajor_W4F0CusMinor_get, _ydlidar.LaserDebug_W3F4CusMajor_W4F0CusMinor_set)
    W4F3Model_W3F0DebugInfTranVer = property(_ydlidar.LaserDebug_W4F3Model_W3F0DebugInfTranVer_get, _ydlidar.LaserDebug_W4F3Model_W3F0DebugInfTranVer_set)
    W3F4HardwareVer_W4F0FirewareMajor = property(_ydlidar.LaserDebug_W3F4HardwareVer_W4F0FirewareMajor_get, _ydlidar.LaserDebug_W3F4HardwareVer_W4F0FirewareMajor_set)
    W7F0FirewareMinor = property(_ydlidar.LaserDebug_W7F0FirewareMinor_get, _ydlidar.LaserDebug_W7F0FirewareMinor_set)
    W3F4BoradHardVer_W4F0Moth = property(_ydlidar.LaserDebug_W3F4BoradHardVer_W4F0Moth_get, _ydlidar.LaserDebug_W3F4BoradHardVer_W4F0Moth_set)
    W2F5Output2K4K5K_W5F0Date = property(_ydlidar.LaserDebug_W2F5Output2K4K5K_W5F0Date_get, _ydlidar.LaserDebug_W2F5Output2K4K5K_W5F0Date_set)
    W1F6GNoise_W1F5SNoise_W1F4MotorCtl_W4F0SnYear = property(_ydlidar.LaserDebug_W1F6GNoise_W1F5SNoise_W1F4MotorCtl_W4F0SnYear_get, _ydlidar.LaserDebug_W1F6GNoise_W1F5SNoise_W1F4MotorCtl_W4F0SnYear_set)
    W7F0SnNumH = property(_ydlidar.LaserDebug_W7F0SnNumH_get, _ydlidar.LaserDebug_W7F0SnNumH_set)
    W7F0SnNumL = property(_ydlidar.LaserDebug_W7F0SnNumL_get, _ydlidar.LaserDebug_W7F0SnNumL_set)
    W7F0Health = property(_ydlidar.LaserDebug_W7F0Health_get, _ydlidar.LaserDebug_W7F0Health_set)
    W3F4CusHardVer_W4F0CusSoftVer = property(_ydlidar.LaserDebug_W3F4CusHardVer_W4F0CusSoftVer_get, _ydlidar.LaserDebug_W3F4CusHardVer_W4F0CusSoftVer_set)
    W7F0LaserCurrent = property(_ydlidar.LaserDebug_W7F0LaserCurrent_get, _ydlidar.LaserDebug_W7F0LaserCurrent_set)
    MaxDebugIndex = property(_ydlidar.LaserDebug_MaxDebugIndex_get, _ydlidar.LaserDebug_MaxDebugIndex_set)

    def __init__(self):
        _ydlidar.LaserDebug_swiginit(self, _ydlidar.new_LaserDebug())
    __swig_destroy__ = _ydlidar.delete_LaserDebug

# Register LaserDebug in _ydlidar:
_ydlidar.LaserDebug_swigregister(LaserDebug)

class LaserScan(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    stamp = property(_ydlidar.LaserScan_stamp_get, _ydlidar.LaserScan_stamp_set)
    points = property(_ydlidar.LaserScan_points_get, _ydlidar.LaserScan_points_set)
    config = property(_ydlidar.LaserScan_config_get, _ydlidar.LaserScan_config_set)

    def __init__(self):
        _ydlidar.LaserScan_swiginit(self, _ydlidar.new_LaserScan())
    __swig_destroy__ = _ydlidar.delete_LaserScan

# Register LaserScan in _ydlidar:
_ydlidar.LaserScan_swigregister(LaserScan)

YDLIDAR_TYPE_SERIAL = _ydlidar.YDLIDAR_TYPE_SERIAL
YDLIDAR_TYPE_TCP = _ydlidar.YDLIDAR_TYPE_TCP
YDLIDAR_TYPC_UDP = _ydlidar.YDLIDAR_TYPC_UDP
TYPE_TOF = _ydlidar.TYPE_TOF
TYPE_TRIANGLE = _ydlidar.TYPE_TRIANGLE
TYPE_TOF_NET = _ydlidar.TYPE_TOF_NET
TYPE_Tail = _ydlidar.TYPE_Tail
LidarPropSerialPort = _ydlidar.LidarPropSerialPort
LidarPropIgnoreArray = _ydlidar.LidarPropIgnoreArray
LidarPropSerialBaudrate = _ydlidar.LidarPropSerialBaudrate
LidarPropLidarType = _ydlidar.LidarPropLidarType
LidarPropDeviceType = _ydlidar.LidarPropDeviceType
LidarPropSampleRate = _ydlidar.LidarPropSampleRate
LidarPropAbnormalCheckCount = _ydlidar.LidarPropAbnormalCheckCount
LidarPropMaxRange = _ydlidar.LidarPropMaxRange
LidarPropMinRange = _ydlidar.LidarPropMinRange
LidarPropMaxAngle = _ydlidar.LidarPropMaxAngle
LidarPropMinAngle = _ydlidar.LidarPropMinAngle
LidarPropScanFrequency = _ydlidar.LidarPropScanFrequency
LidarPropFixedResolution = _ydlidar.LidarPropFixedResolution
LidarPropReversion = _ydlidar.LidarPropReversion
LidarPropInverted = _ydlidar.LidarPropInverted
LidarPropAutoReconnect = _ydlidar.LidarPropAutoReconnect
LidarPropSingleChannel = _ydlidar.LidarPropSingleChannel
LidarPropIntenstiy = _ydlidar.LidarPropIntenstiy
LidarPropSupportMotorDtrCtrl = _ydlidar.LidarPropSupportMotorDtrCtrl
class YDLidar(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    lidar = property(_ydlidar.YDLidar_lidar_get, _ydlidar.YDLidar_lidar_set)

    def __init__(self):
        _ydlidar.YDLidar_swiginit(self, _ydlidar.new_YDLidar())
    __swig_destroy__ = _ydlidar.delete_YDLidar

# Register YDLidar in _ydlidar:
_ydlidar.YDLidar_swigregister(YDLidar)

class LaserPoint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    angle = property(_ydlidar.LaserPoint_angle_get, _ydlidar.LaserPoint_angle_set)
    range = property(_ydlidar.LaserPoint_range_get, _ydlidar.LaserPoint_range_set)
    intensity = property(_ydlidar.LaserPoint_intensity_get, _ydlidar.LaserPoint_intensity_set)

    def __init__(self):
        _ydlidar.LaserPoint_swiginit(self, _ydlidar.new_LaserPoint())
    __swig_destroy__ = _ydlidar.delete_LaserPoint

# Register LaserPoint in _ydlidar:
_ydlidar.LaserPoint_swigregister(LaserPoint)

class LaserConfig(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    min_angle = property(_ydlidar.LaserConfig_min_angle_get, _ydlidar.LaserConfig_min_angle_set)
    max_angle = property(_ydlidar.LaserConfig_max_angle_get, _ydlidar.LaserConfig_max_angle_set)
    angle_increment = property(_ydlidar.LaserConfig_angle_increment_get, _ydlidar.LaserConfig_angle_increment_set)
    time_increment = property(_ydlidar.LaserConfig_time_increment_get, _ydlidar.LaserConfig_time_increment_set)
    scan_time = property(_ydlidar.LaserConfig_scan_time_get, _ydlidar.LaserConfig_scan_time_set)
    min_range = property(_ydlidar.LaserConfig_min_range_get, _ydlidar.LaserConfig_min_range_set)
    max_range = property(_ydlidar.LaserConfig_max_range_get, _ydlidar.LaserConfig_max_range_set)

    def __init__(self):
        _ydlidar.LaserConfig_swiginit(self, _ydlidar.new_LaserConfig())
    __swig_destroy__ = _ydlidar.delete_LaserConfig

# Register LaserConfig in _ydlidar:
_ydlidar.LaserConfig_swigregister(LaserConfig)

class LaserFan(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    stamp = property(_ydlidar.LaserFan_stamp_get, _ydlidar.LaserFan_stamp_set)
    npoints = property(_ydlidar.LaserFan_npoints_get, _ydlidar.LaserFan_npoints_set)
    points = property(_ydlidar.LaserFan_points_get, _ydlidar.LaserFan_points_set)
    config = property(_ydlidar.LaserFan_config_get, _ydlidar.LaserFan_config_set)

    def __init__(self):
        _ydlidar.LaserFan_swiginit(self, _ydlidar.new_LaserFan())
    __swig_destroy__ = _ydlidar.delete_LaserFan

# Register LaserFan in _ydlidar:
_ydlidar.LaserFan_swigregister(LaserFan)

class string_t(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    data = property(_ydlidar.string_t_data_get, _ydlidar.string_t_data_set)

    def __init__(self):
        _ydlidar.string_t_swiginit(self, _ydlidar.new_string_t())
    __swig_destroy__ = _ydlidar.delete_string_t

# Register string_t in _ydlidar:
_ydlidar.string_t_swigregister(string_t)

class LidarPort(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    port = property(_ydlidar.LidarPort_port_get, _ydlidar.LidarPort_port_set)

    def __init__(self):
        _ydlidar.LidarPort_swiginit(self, _ydlidar.new_LidarPort())
    __swig_destroy__ = _ydlidar.delete_LidarPort

# Register LidarPort in _ydlidar:
_ydlidar.LidarPort_swigregister(LidarPort)

class LidarVersion(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    hardware = property(_ydlidar.LidarVersion_hardware_get, _ydlidar.LidarVersion_hardware_set)
    soft_major = property(_ydlidar.LidarVersion_soft_major_get, _ydlidar.LidarVersion_soft_major_set)
    soft_minor = property(_ydlidar.LidarVersion_soft_minor_get, _ydlidar.LidarVersion_soft_minor_set)
    soft_patch = property(_ydlidar.LidarVersion_soft_patch_get, _ydlidar.LidarVersion_soft_patch_set)
    sn = property(_ydlidar.LidarVersion_sn_get, _ydlidar.LidarVersion_sn_set)

    def __init__(self):
        _ydlidar.LidarVersion_swiginit(self, _ydlidar.new_LidarVersion())
    __swig_destroy__ = _ydlidar.delete_LidarVersion

# Register LidarVersion in _ydlidar:
_ydlidar.LidarVersion_swigregister(LidarVersion)


def LaserFanInit(to_init):
    return _ydlidar.LaserFanInit(to_init)

def LaserFanDestroy(to_destroy):
    return _ydlidar.LaserFanDestroy(to_destroy)


