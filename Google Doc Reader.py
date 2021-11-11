from __future__ import print_function

import webbrowser
from time import sleep
from apiclient import discovery
from httplib2 import Http
from oauth2client import client
from oauth2client import file
from oauth2client import tools

link = "https://www.google.com/search?q=cat&tbm=isch&ved=2ahUKEwjVnOWeiefrAhUW8awKHSSjAzoQ2-cCegQIABAA&oq=cat&gs_lcp=CgNpbWcQAzIECCMQJzIECCMQJzIECAAQQzIECAAQQzIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQMyBQgAELEDMgIIAFCNFliNFmDhF2gAcAB4AIABOogBOpIBATGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=oY5eX5XIBJbiswWkxo7QAw&bih=975&biw=1920&rlz=1C1CHBF_enUS805US805&safe=strict#imgrc=zP4N2WyGyDNkkM"

search = str(input("Choose a key word: "))

SCOPES = 'https://www.googleapis.com/auth/documents.readonly'
DISCOVERY_DOC = 'https://docs.googleapis.com/$discovery/rest?version=v1'
DOCUMENT_ID = '1H0gAsNZbk42C-Ao5elFPYLIs6ddTThe35rmtWA5rNQc'

i = 0
while i <= 1:
    
    SCOPES = 'https://www.googleapis.com/auth/documents.readonly'
    DISCOVERY_DOC = 'https://docs.googleapis.com/$discovery/rest?version=v1'
    DOCUMENT_ID = '1H0gAsNZbk42C-Ao5elFPYLIs6ddTThe35rmtWA5rNQc'

    def get_credentials():
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth 2.0 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        store = file.Storage('token.json')
        credentials = store.get()

        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            credentials = tools.run_flow(flow, store)
        return credentials

    def read_paragraph_element(element):
        """Returns the text in the given ParagraphElement.

            Args:
                element: a ParagraphElement from a Google Doc.
        """
        text_run = element.get('textRun')
        if not text_run:
            return ''
        return text_run.get('content')


    def read_strucutural_elements(elements):
        """Recurses through a list of Structural Elements to read a document's text where text may be
            in nested elements.

            Args:
                elements: a list of Structural Elements.
        """
        text = ''
        for value in elements:
            if 'paragraph' in value:
                elements = value.get('paragraph').get('elements')
                for elem in elements:
                    text += read_paragraph_element(elem)
            elif 'table' in value:
                # The text in table cells are in nested Structural Elements and tables may be
                # nested.
                table = value.get('table')
                for row in table.get('tableRows'):
                    cells = row.get('tableCells')
                    for cell in cells:
                        text += read_strucutural_elements(cell.get('content'))
            elif 'tableOfContents' in value:
                # The text in the TOC is also in a Structural Element.
                toc = value.get('tableOfContents')
                text += read_strucutural_elements(toc.get('content'))
        return text


    def main():
        """Uses the Docs API to print out the text of a document."""
        credentials = get_credentials()
        http = credentials.authorize(Http())
        docs_service = discovery.build(
            'docs', 'v1', http=http, discoveryServiceUrl=DISCOVERY_DOC)
        doc = docs_service.documents().get(documentId=DOCUMENT_ID).execute()
        doc_content = doc.get('body').get('content')
        words = (read_strucutural_elements(doc_content))   
        
        wordsList = (words.split())
        #print(wordsList)
        #print(words[0])     #Finds a single letter
        #print(wordsList[0]) #Finds a single word      
        for a in wordsList:
            if a == search:
                print("The word " + a + " was found!")
                webbrowser.open(link)
                print(wordsList)
                i = i + 1    
        sleep(4)        

        #z = 0
        #while z <= 1:
            #length = (len(wordsList))
            #if length >= 15:
                #for b in wordsList[z + 15]:
                    #print(b)
                    #z = z + 1

        # TODO Add word count limit 

    if __name__ == '__main__':
        main()
sleep(5)