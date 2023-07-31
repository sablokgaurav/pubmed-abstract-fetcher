from urllib.request import urlopen
from bs4 import BeautifulSoup
def ncbiAbstractMiner():
    """summary_line
    this function will bring all the abstract from the ncbi to your 
    desk, you can call this function and it will ask for the ncbi
    pubmed ids and will download the abstract for them.
    Keyword arguments:
    argument -- description
    it takes the ncbi ids from the user as input
    Return: return_description
    it returns a tuple with the ncbi id and the 
    corresponding abstract for the language model
    building or text analysis or building an corpus.
    """
    ncbi_id_list = []
    while True:
        take_ncbi_ids = input("Please enter the ncbi ids for which \
                                    you want to have the abstract for the corpus")
        ncbi_id_list.append(take_ncbi_ids)
        if take_ncbi_ids == "":
            break
    format_id_links = []
    for i in range(len(ncbi_id_list)):
        format_id_links.append(f"https://pubmed.ncbi.nlm.nih.gov/{ncbi_id_list[i]}/")
    ncbi_derive_information = {}
    for i in range(len(format_id_links)):
        ncbi_derive_information[ncbi_id_list[i]] = ''.join([i.get_text().strip() \
                for i in BeautifulSoup(urlopen(format_id_links[i]), \
                        "html.parser").find_all("div", class_ = "abstract-content selected")])
    return [(k,v) for k,v in ncbi_derive_information.items() if k or v != ""]  


def ncbiAbstractMiner(file):
    """summary_line
    this is a file version of the ncbi_abstract_miner which 
    will bring all the abstract from the ncbi to your 
    desk, you can specify a file with the ncbi pubmed ids 
    and will download the abstract for them.
    Keyword arguments:
    argument -- description
    it takes the ncbi ids from the user as input
    Return: return_description
    it returns a tuple with the ncbi id and the 
    corresponding abstract for the language model
    building or text analysis or building an corpus.
    """
    ncbi_id_list = []
    with open(file, "r") as ncbi_ids:
        for line in ncbi_ids.readlines():
            ncbi_id_list.append(line.strip())
        ncbi_ids.close()
    format_id_links = []
    for i in range(len(ncbi_id_list)):
        format_id_links.append(f"https://pubmed.ncbi.nlm.nih.gov/{ncbi_id_list[i]}/")
    ncbi_derive_information = {}
    for i in range(len(format_id_links)):
        ncbi_derive_information[ncbi_id_list[i]] = ''.join([i.get_text().strip() \
                for i in BeautifulSoup(urlopen(format_id_links[i]), \
                        "html.parser").find_all("div", class_ = "abstract-content selected")])
    return [(k,v) for k,v in ncbi_derive_information.items() if k or v != ""] 
