import numpy as np
from grispy import GriSPy
import pytest


def test_distance_A_01():
    # Distancia a-->b = b-->a (metric='euclid')
    data = np.random.uniform(-10, 10, size=(10, 2))
    periodic = {0: None, 1: None}
    gsp = GriSPy(
        data=data,
        N_cells=2,
        copy_data=False,
        periodic=periodic,
        metric="euclid",
        load_grid=None,
    )
    dist1 = gsp.distance(np.array([1, 1]), np.array([[2, 2]]))
    dist2 = gsp.distance(np.array([2, 2]), np.array([[1, 1]]))
    np.testing.assert_almost_equal(dist1, dist2, decimal=16)


def test_distance_A_02():
    # Distancia a-->b = b-->a (metric='sphere')
    data = np.random.uniform(-10, 10, size=(10, 2))
    periodic = {0: None, 1: None}
    gsp = GriSPy(
        data=data,
        N_cells=2,
        copy_data=False,
        periodic=periodic,
        metric="sphere",
        load_grid=None,
    )
    dist1 = gsp.distance(np.array([1, 1]), np.array([[2, 2]]))
    dist2 = gsp.distance(np.array([2, 2]), np.array([[1, 1]]))
    np.testing.assert_almost_equal(dist1, dist2, decimal=10)


def test_distance_B_01():
    # Distancia a-->c <= a-->b + b-->c (metric='euclid')
    data = np.random.uniform(-10, 10, size=(10, 2))
    periodic = {0: None, 1: None}
    gsp = GriSPy(
        data=data,
        N_cells=2,
        copy_data=False,
        periodic=periodic,
        metric="euclid",
        load_grid=None,
    )
    p_a = [1, 1]
    p_b = [2, 2]
    p_c = [1, 2]
    dist_ab = gsp.distance(np.array(p_a), np.array([p_b]))
    dist_ac = gsp.distance(np.array(p_a), np.array([p_c]))
    dist_bc = gsp.distance(np.array(p_b), np.array([p_c]))
    assert dist_ac <= dist_ab + dist_bc


def test_distance_B_02():
    # Distancia a-->c <= a-->b + b-->c (metric='sphere')
    data = np.random.uniform(-10, 10, size=(10, 2))
    periodic = {0: None, 1: None}
    gsp = GriSPy(
        data=data,
        N_cells=2,
        copy_data=False,
        periodic=periodic,
        metric="sphere",
        load_grid=None,
    )
    p_a = [1, 1]
    p_b = [2, 2]
    p_c = [1, 2]
    dist_ab = gsp.distance(np.array(p_a), np.array([p_b]))
    dist_ac = gsp.distance(np.array(p_a), np.array([p_c]))
    dist_bc = gsp.distance(np.array(p_b), np.array([p_c]))
    assert dist_ac <= dist_ab + dist_bc


def test_distance_C_01():
    # Distancias >= 0 (metric='euclid')
    data = np.random.uniform(-10, 10, size=(50, 2))
    periodic = {0: None, 1: None}
    gsp = GriSPy(
        data=data,
        N_cells=2,
        copy_data=False,
        periodic=periodic,
        metric="euclid",
        load_grid=None,
    )
    centre_0 = np.random.uniform(-10, 10, size=(2,))
    dist = gsp.distance(centre_0, data)
    assert (dist >= 0).all()


def test_distance_C_02():
    # Distancias >= 0 (metric='sphere')
    data = np.random.uniform(-10, 10, size=(50, 2))
    periodic = {0: None, 1: None}
    gsp = GriSPy(
        data=data,
        N_cells=2,
        copy_data=False,
        periodic=periodic,
        metric="sphere",
        load_grid=None,
    )
    centre_0 = np.random.uniform(-10, 10, size=(2,))
    dist = gsp.distance(centre_0, data)
    assert (dist >= 0).all()


def test_distance_D_01():
    # Distancias != NaN (metric='euclid')
    data = np.random.uniform(-10, 10, size=(50, 2))
    periodic = {0: None, 1: None}
    gsp = GriSPy(
        data=data,
        N_cells=2,
        copy_data=False,
        periodic=periodic,
        metric="euclid",
        load_grid=None,
    )
    centre_0 = np.random.uniform(-10, 10, size=(2,))
    dist = gsp.distance(centre_0, data)
    assert not np.isnan(dist).any()


def test_distance_D_02():
    # Distancias != NaN (metric='sphere')
    data = np.random.uniform(-10, 10, size=(50, 2))
    periodic = {0: None, 1: None}
    gsp = GriSPy(
        data=data,
        N_cells=2,
        copy_data=False,
        periodic=periodic,
        metric="sphere",
        load_grid=None,
    )
    centre_0 = np.random.uniform(-10, 10, size=(2,))
    dist = gsp.distance(centre_0, data)
    assert not np.isnan(dist).any()


def test__init__A_01():
    # Data type
    data = 4
    periodic = {0: None, 1: None}
    with pytest.raises(TypeError, match=r".*must be a numpy array*"):
        gsp = GriSPy(
            data=data,
            N_cells=2,
            copy_data=False,
            periodic=periodic,
            metric="sphere",
            load_grid=None,
        )


def test__init__A_02():
    # Data format
    data = np.array([])
    periodic = {0: None, 1: None}
    with pytest.raises(
        ValueError, match=r".*Data array has the wrong shape*"
    ):
        gsp = GriSPy(
            data=data,
            N_cells=2,
            copy_data=False,
            periodic=periodic,
            metric="sphere",
            load_grid=None,
        )


def test__init__A_03():
    # Data format
    data = np.array([1, 1, 1])
    periodic = {0: None, 1: None}
    with pytest.raises(
        ValueError, match=r".*Data array has the wrong shape*"
    ):
        gsp = GriSPy(
            data=data,
            N_cells=2,
            copy_data=False,
            periodic=periodic,
            metric="sphere",
            load_grid=None,
        )


def test__init__A_04():
    # Data value
    data = np.array([[]])
    periodic = {0: None, 1: None}
    with pytest.raises(
        ValueError, match=r".*Data must have at least 1 point*"
    ):
        gsp = GriSPy(
            data=data,
            N_cells=2,
            copy_data=False,
            periodic=periodic,
            metric="sphere",
            load_grid=None,
        )
