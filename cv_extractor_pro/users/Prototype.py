import textract
import logging 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def extract_doc_text(doc_path):
    try:
        text = textract.process(doc_path).decode('utf-8')
        logger.debug(f"Extracted text from DOC {doc_path}: {text[:500]}")
        return text
    except Exception as e:
        logger.error(f"Error extracting text from doc: {e}")
        return ""
    
doc_path = 'D:/Sample2/MINTUKMUAR.doc'
extracted_text = extract_doc_text(doc_path)
if extracted_text:
    print("Text extraction successful.")
else:
    print("Text extraction failed.")