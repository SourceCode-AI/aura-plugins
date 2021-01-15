"""
DUMP of the code from aura tests after removing the binwalk integration
"""


@pytest.fixture()
def skip_binwalk():
    from aura.exceptions import FeatureDisabled

    try:
        from aura.analyzers import binwalk_analyzer

        m = mock.MagicMock()
        m.return_value = False
        binwalk_analyzer.can_process_location = m
        yield m
    except FeatureDisabled:
        yield




