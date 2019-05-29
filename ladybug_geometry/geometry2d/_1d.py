# coding=utf-8
"""Base class for all 1D geometries in 2D space (Ray2D and LineSegment2D)."""
from __future__ import division

from .pointvector import Vector2D, Point2D
from ..intersection2d import intersect_line2d, closest_point2d_on_line2d


class Base1DIn2D(object):
    """Base class for all 1D geometries in 2D space (Ray2D and LineSegment2D).

    Properties:
        p: End Point2D of object
        v: Vector2D along object
    """

    def __init__(self, p, v):
        """Initilize Base1DIn2D.

        Args:
            p: A Point2D representing the base.
            v: A Vector2D representing the direction.
        """
        assert isinstance(p, Point2D), "Expected Point2D. Got {}.".format(type(p))
        assert isinstance(v, Vector2D), "Expected Vector2D. Got {}.".format(type(v))
        self._p = p
        self._v = v

    @property
    def p(self):
        """Base point."""
        return self._p

    @property
    def v(self):
        """Direction vector."""
        return self._v

    def closest_point(self, point):
        """Get the closest Point2D on this object to another Point2D.

        Args:
            point: A Point2D object to which the closest point on this object
                will be computed.

        Returns:
            Point2D for the closest point on this line to the input point.
        """
        return closest_point2d_on_line2d(point, self)

    def distance_to_point(self, point):
        """Get the minimum distance between this object and the input point.

        Args:
            point: A Point2D object to which the minimum distance will be computed.

        Returns:
            The distance to the input point.
        """
        close_pt = self.closest_point(point)
        return point.distance_to_point(close_pt)

    def intersect_line_ray(self, line_ray):
        """Get the intersection between this object and another Ray2 or LineSegment2D.

        Args:
            line_ray: Another LineSegment2D or Ray2D or to intersect.

        Returns:
            Point2D of intersection if it exists. None if no intersection exists.
        """
        return intersect_line2d(self, line_ray)

    def duplicate(self):
        """Get a copy of this object."""
        return self.__copy__()

    def __copy__(self):
        return self.__class__(self.p, self.v)

    def ToString(self):
        """Overwrite .NET ToString."""
        return self.__repr__()

    def __repr__(self):
        """Base1Din2D representation."""
        return 'Base 1D Object (2D Space)'