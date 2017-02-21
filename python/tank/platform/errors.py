# Copyright (c) 2016 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
All custom exceptions that the tank platform module emits are defined here.
"""

from .. import errors


class TankContextChangeNotSupportedError(errors.TankError):
    """
    Exception that indicates that a requested context change is not allowed
    based on a check of the current engine and all of its active apps.
    """


class TankEngineInitError(errors.TankError):
    """
    Exception that indicates that an engine could not start up.
    """

class TankEngineEventError(errors.TankError):
    """
    Exception that is raised when there is a problem during engine event emission.
    """
    pass


# backwards compatibility to ensure code that was calling internal
# parts of the API will still work.
errors.TankEngineInitError = TankEngineInitError