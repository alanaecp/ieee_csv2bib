import csv

def toBib(dic):

    paper_id =  dic['authors'].split(';')[0].replace('.','').replace(' ','') + '_' +   dic['document_title'].split()[0] + '_' +  dic['document_title'].split()[1] + str( dic['publication_year'])

    return '''
    @inproceedings# {paper_id},
        author = # {authors} $,
        title = # {document_title} $,
        booktitle = # {publication_title} $,
        year = # {publication_year} $,
        issn = # {issn} $,
        abstract = # {abstract} $,
        pages = # {start_page} --  {end_page} $,
        doi = # {doi} $,
        publisher = # {publisher} $,
        keywords = # {author_keywords} $
    $
    '''.format(
        paper_id = paper_id,
        document_title = dic['document_title'],
        authors = dic['authors'],
        publication_title = dic['publication_title'],
        publication_year = dic['publication_year'],
        abstract = dic['abstract'],
        doi = dic['doi'],
        publisher= dic['publisher'],
        author_keywords = dic['author_keywords'],
        isbns = dic['isbns'],
        issn = dic['issn'],
        start_page = dic['start_page'],
        end_page = dic['end_page'],
     ).replace('#','{').replace('$','}')


referencias = ''
with open('IEEE.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        dic = {}

        if line_count == 0:
            print("-------------------")
            line_count += 1
        else:
            dic['document_title'] = row[0]
            dic['authors'] = row[1]
            dic['author_affiliations'] = row[2]
            dic['publication_title'] = row[3]
            dic['date_added_to_xplore'] = row[4]
            dic['publication_year'] = row[5]
            dic['volume'] = row[6]
            dic['issue'] = row[7]
            dic['start_page'] = row[8]
            dic['end_page'] = row[9]
            dic['abstract'] = row[10]
            dic['issn'] = row[11]
            dic['isbns'] = row[12]
            dic['doi'] = row[13]
            dic['funding_information'] = row[14]
            dic['pdf_link'] = row[15]
            dic['author_keywords'] = row[16]
            dic['ieee_terms'] = row[17]
            dic['inspec_controlled_terms'] = row[18]
            dic['inspec_non-controlled_terms'] = row[19]
            dic['mesh_terms'] = row[20]
            dic['article_citation_count'] = row[21]
            dic['reference_count'] = row[22]
            dic['license'] = row[23]
            dic['online_date'] = row[24]
            dic['issue_date'] = row[25]
            dic['meeting_date'] = row[26]
            dic['publisher'] = row[27]
            dic['document_identifier'] = row[28]


            referencias += toBib(dic)


            line_count += 1

print('TOTAL: ', line_count)

'''
Salvar um arquivo .bib com os dados processados

'''
filename = 'output.bib'

with open(filename, 'w') as f:
    print(referencias, file=f)  # Python 3.x
