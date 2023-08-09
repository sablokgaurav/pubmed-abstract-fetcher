# pubmed_indexer_abstract_fetcher
This function will prepare the abstract and the id information for all the [pubmed](https://pubmed.ncbi.nlm.nih.gov) articles that you want to read and have as a citation. I coded this using a web scraping approach and it is blazing fast and parses better than ncbi eutils. You can give any ncbi pubmed id single or pass it through the file and it will download and prepare the citations, abstract and also the corpus for the language data.

Gaurav Sablok \
Frontiers: https://loop.frontiersin.org/people/33293/overview \
ORCID: https://orcid.org/0000-0002-4157-9405 \
WOS: https://www.webofscience.com/wos/author/record/C-5940-2014 \
Github:https://github.com/sablokgaurav \
Linkedin: https://www.linkedin.com/in/sablokgaurav/

```python
ncbiAbstractMiner()
[('18980659',
  'The Arabidopsis thaliana genome contains hundreds of genes essential for seed development.
Because null mutations in these genes cause embryo lethality,  their specific molecular and developmental
functions are largely unknown. Here, we identify a role for EMB1611/MEE22, an essential
gene in Arabidopsis, in shoot apical meristem maintenance. EMB1611 encodes a large,
novel protein with N-terminal coiled-coil regions and two putative transmembrane domains.
We show that the partial loss-of-function emb1611-2 mutation causes a range of pleiotropic
developmental phenotypes, most dramatically a progressive loss of shoot apical meristem
function that causes premature meristem termination. emb1611-2 plants display disorganization
of the shoot meristem cell layers early in development, and an associated stem cell
fate change to an organogenic identity. Genetic and molecular analysis indicates
that EMB1611 is required for maintenance of the CLV-WUS stem cell regulatory pathway
in the shoot meristem, but also has WUS-independent activity. In addition,
emb1611-2 plants have reduced shoot and root growth, and their rosette leaves form trichomes with extra branches,
 a defect we associate with an increase in endoreduplication. Our data indicate
that EMB1611 functions to maintain cells, particularly those in the shoot meristem,
roots and developing rosette leaves, in a proliferative or uncommitted state.')]
```

```python
ncbiAbstractMiner(file)
You can pass a file with endless pubmed ids.

