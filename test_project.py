import os
import tempfile
import pytest
from project import check_csv, read_csv, create_qrcode, create_pdf

@pytest.fixture
def csv_data():
    csv_content = "link1, string1\nlink2, string2\n"
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(csv_content)
        temp_file.flush()
        yield temp_file.name
    os.unlink(temp_file.name)

def test_create_qrcode():
    qr_code = create_qrcode("test_link")
    assert qr_code is not None

def test_create_pdf():
    # Create a temporary PDF file
    pdf_file = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
    create_pdf("test_link", "Test String", create_qrcode("test_link"))
    assert os.path.isfile(pdf_file.name)

if __name__ == "__main__":
    pytest.main()
