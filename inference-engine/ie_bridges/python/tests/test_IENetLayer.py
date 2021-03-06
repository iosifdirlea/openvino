import warnings
import numpy

from openvino.inference_engine import DataPtr, IECore
from conftest import model_path


test_net_xml, test_net_bin = model_path()


def test_name(recwarn):
    warnings.simplefilter("always")
    ie = IECore()
    net = ie.read_network(model=test_net_xml, weights=test_net_bin)
    assert net.layers['27'].name == "27"
    assert len(recwarn) == 1
    assert recwarn.pop(DeprecationWarning)


def test_type(recwarn):
    warnings.simplefilter("always")
    ie = IECore()
    net = ie.read_network(model=test_net_xml, weights=test_net_bin)
    assert net.layers['27'].type == "Pooling"
    assert len(recwarn) == 1
    assert recwarn.pop(DeprecationWarning)


def test_affinity_getter(recwarn):
    warnings.simplefilter("always")
    ie = IECore()
    net = ie.read_network(model=test_net_xml, weights=test_net_bin)
    assert net.layers['27'].affinity == ""
    assert len(recwarn) == 1
    assert recwarn.pop(DeprecationWarning)


def test_affinity_setter(recwarn):
    warnings.simplefilter("always")
    ie = IECore()
    net = ie.read_network(model=test_net_xml, weights=test_net_bin)
    net.layers['27'].affinity = "CPU"
    assert net.layers['27'].affinity == "CPU"
    assert len(recwarn) == 2
    assert recwarn.pop(DeprecationWarning)


def test_blobs(recwarn):
    warnings.simplefilter("always")
    ie = IECore()
    net = ie.read_network(model=test_net_xml, weights=test_net_bin)
    assert isinstance(net.layers['19/Fused_Add_'].blobs["biases"], numpy.ndarray)
    assert isinstance(net.layers['19/Fused_Add_'].blobs["weights"], numpy.ndarray)
    assert net.layers['19/Fused_Add_'].blobs["biases"].size != 0
    assert net.layers['19/Fused_Add_'].blobs["weights"].size != 0
    assert len(recwarn) == 4
    assert recwarn.pop(DeprecationWarning)


def test_params_getter(recwarn):
    warnings.simplefilter("always")
    ie = IECore()
    net = ie.read_network(model=test_net_xml, weights=test_net_bin)
    assert net.layers['27'].params == {"kernel" : "2,2", "pads_begin" : "0,0",
                                       "pads_end" : "0,0", "rounding_type" : "floor",
                                       "strides" : "2,2", "pool-method" : "max",
                                       "originalLayersNames" : "27"}
    assert len(recwarn) == 1
    assert recwarn.pop(DeprecationWarning)


def test_params_setter(recwarn):
    warnings.simplefilter("always")
    ie = IECore()
    net = ie.read_network(model=test_net_xml, weights=test_net_bin)
    params = net.layers['27'].params
    params.update({'PrimitivesPriority': 'cpu:ref_any'})
    net.layers['27'].params = params
    assert net.layers['27'].params == {"kernel" : "2,2", "pads_begin" : "0,0",
                                       "pads_end" : "0,0", "rounding_type" : "floor",
                                       "strides" : "2,2", "pool-method" : "max",
                                       "originalLayersNames" : "27", 'PrimitivesPriority': 'cpu:ref_any'}
    assert len(recwarn) == 3
    assert recwarn.pop(DeprecationWarning)


def test_out_data(recwarn):
    warnings.simplefilter("always")
    ie = IECore()
    net = ie.read_network(model=test_net_xml, weights=test_net_bin)
    assert isinstance(net.layers['27'].out_data[0], DataPtr)
    assert len(recwarn) == 1
    assert recwarn.pop(DeprecationWarning)


def test_in_data(recwarn):
    warnings.simplefilter("always")
    ie = IECore()
    net = ie.read_network(model=test_net_xml, weights=test_net_bin)
    assert isinstance(net.layers['27'].in_data[0], DataPtr)
    assert len(recwarn) == 1
    assert recwarn.pop(DeprecationWarning)


def test_parents(recwarn):
    warnings.simplefilter("always")
    ie = IECore()
    net = ie.read_network(model=test_net_xml, weights=test_net_bin)
    parents = net.layers['27'].parents
    assert len(parents) == 1
    assert(parents[0] == '26')
    assert len(recwarn) == 1
    assert recwarn.pop(DeprecationWarning)


def test_children(recwarn):
    warnings.simplefilter("always")
    ie = IECore()
    net = ie.read_network(model=test_net_xml, weights=test_net_bin)
    children = net.layers['26'].children
    assert len(children) == 1
    assert(children[0] == '27')
    assert len(recwarn) == 1
    assert recwarn.pop(DeprecationWarning)
