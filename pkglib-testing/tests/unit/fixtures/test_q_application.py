import pytest

QT = False
try:
    from pkglib_testing.pytest.q_application import q_application  # @UnusedImport  # NOQA
    from PyQt4 import QtGui
    QT = True
except:
    pass

@pytest.mark.skipif(not QT, reason="QT unavailable")
def test_q_application(q_application):
    assert QtGui.QX11Info.display()
