from ocr_check_nld import __version__
from ocr_check_nld import Check
import os


def test_version():
    assert __version__ == '0.1.0'


def test_sample_checks():
    LANG = "eng"
    script_path = os.path.dirname(os.path.realpath(__file__))
    sample_checks_paths = (script_path + "/receipt-5c331e50qmpob2z7-761-2124959.jpg",
                           script_path + "/receipt-2combined-5c331959weobocc6-581-1049079.jpg",
                           script_path + "/receipt-5c331f9au5zwciuv-880-2102991.jpg")
    sample_checks_totals = (33.98,
                            72.74,
                            -1.0)
    
    for check_path, check_total in zip(sample_checks_paths, sample_checks_totals):
        check = Check(check_path, LANG)
        total = check.get_total()
        
        assert total == check_total
    
