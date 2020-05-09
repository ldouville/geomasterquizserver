import codecs

def get(url):
    if url in URL_DICT.keys():
        file_path = f"scraping/{URL_DICT[url]}"
        file = codecs.open(file_path, "r", "utf-8")
        html = file.read()
        file.close()
        return html
        

URL_DICT = {
    'https://fr.wikipedia.org/wiki/Liste_des_pays_du_monde': 'html/pays.html',
    'https://fr.wikipedia.org/wiki/Afghanistan': 'html/Afghanistan.html',
    'https://fr.wikipedia.org/wiki/Afrique_du_Sud': 'html/Afrique_du_Sud.html',
    'https://fr.wikipedia.org/wiki/Albanie': 'html/Albanie.html',
    'https://fr.wikipedia.org/wiki/Alg%C3%A9rie': 'html/Alg%C3%A9rie.html',
    'https://fr.wikipedia.org/wiki/Allemagne': 'html/Allemagne.html',
    'https://fr.wikipedia.org/wiki/Andorre': 'html/Andorre.html',
    'https://fr.wikipedia.org/wiki/Angola': 'html/Angola.html',
    'https://fr.wikipedia.org/wiki/Antigua-et-Barbuda': 'html/Antigua-et-Barbuda.html',
    'https://fr.wikipedia.org/wiki/Arabie_saoudite': 'html/Arabie_saoudite.html',
    'https://fr.wikipedia.org/wiki/Argentine': 'html/Argentine.html',
    'https://fr.wikipedia.org/wiki/Arm%C3%A9nie': 'html/Arm%C3%A9nie.html',
    'https://fr.wikipedia.org/wiki/Australie': 'html/Australie.html',
    'https://fr.wikipedia.org/wiki/Autriche': 'html/Autriche.html',
    'https://fr.wikipedia.org/wiki/Azerba%C3%AFdjan': 'html/Azerba%C3%AFdjan.html',
    'https://fr.wikipedia.org/wiki/Bahamas': 'html/Bahamas.html',
    'https://fr.wikipedia.org/wiki/Bahre%C3%AFn': 'html/Bahre%C3%AFn.html',
    'https://fr.wikipedia.org/wiki/Bangladesh': 'html/Bangladesh.html',
    'https://fr.wikipedia.org/wiki/Barbade': 'html/Barbade.html',
    'https://fr.wikipedia.org/wiki/Belgique': 'html/Belgique.html',
    'https://fr.wikipedia.org/wiki/Belize': 'html/Belize.html',
    'https://fr.wikipedia.org/wiki/B%C3%A9nin': 'html/B%C3%A9nin.html',
    'https://fr.wikipedia.org/wiki/Bhoutan': 'html/Bhoutan.html',
    'https://fr.wikipedia.org/wiki/B%C3%A9larus': 'html/B%C3%A9larus.html',
    'https://fr.wikipedia.org/wiki/Birmanie': 'html/Birmanie.html',
    'https://fr.wikipedia.org/wiki/Bolivie': 'html/Bolivie.html',
    'https://fr.wikipedia.org/wiki/Bosnie-Herz%C3%A9govine': 'html/Bosnie-Herz%C3%A9govine.html',
    'https://fr.wikipedia.org/wiki/Botswana': 'html/Botswana.html',
    'https://fr.wikipedia.org/wiki/Br%C3%A9sil': 'html/Br%C3%A9sil.html',
    'https://fr.wikipedia.org/wiki/Brunei': 'html/Brunei.html',
    'https://fr.wikipedia.org/wiki/Bulgarie': 'html/Bulgarie.html',
    'https://fr.wikipedia.org/wiki/Burkina': 'html/Burkina.html',
    'https://fr.wikipedia.org/wiki/Burundi': 'html/Burundi.html',
    'https://fr.wikipedia.org/wiki/Cambodge': 'html/Cambodge.html',
    'https://fr.wikipedia.org/wiki/Cameroun': 'html/Cameroun.html',
    'https://fr.wikipedia.org/wiki/Canada': 'html/Canada.html',
    'https://fr.wikipedia.org/wiki/Cap-Vert': 'html/Cap-Vert.html',
    'https://fr.wikipedia.org/wiki/R%C3%A9publique_centrafricaine': 'html/R%C3%A9publique_centrafricaine.html',
    'https://fr.wikipedia.org/wiki/Chili': 'html/Chili.html',
    'https://fr.wikipedia.org/wiki/R%C3%A9publique_populaire_de_Chine': 'html/R%C3%A9publique_populaire_de_Chine.html',
    'https://fr.wikipedia.org/wiki/Chypre_(pays)': 'html/Chypre_(pays).html',
    'https://fr.wikipedia.org/wiki/Colombie': 'html/Colombie.html',
    'https://fr.wikipedia.org/wiki/Comores_(pays)': 'html/Comores_(pays).html',
    'https://fr.wikipedia.org/wiki/R%C3%A9publique_du_Congo': 'html/R%C3%A9publique_du_Congo.html',
    'https://fr.wikipedia.org/wiki/R%C3%A9publique_d%C3%A9mocratique_du_Congo': 'html/R%C3%A9publique_d%C3%A9mocratique_du_Congo.html',
    'https://fr.wikipedia.org/wiki/%C3%8Eles_Cook': 'html/%C3%8Eles_Cook.html',
    'https://fr.wikipedia.org/wiki/Cor%C3%A9e_du_Nord': 'html/Cor%C3%A9e_du_Nord.html',
    'https://fr.wikipedia.org/wiki/Cor%C3%A9e_du_Sud': 'html/Cor%C3%A9e_du_Sud.html',
    'https://fr.wikipedia.org/wiki/Costa_Rica': 'html/Costa_Rica.html',
    'https://fr.wikipedia.org/wiki/C%C3%B4te_d%27Ivoire': 'html/C%C3%B4te_d%27Ivoire.html',
    'https://fr.wikipedia.org/wiki/Croatie': 'html/Croatie.html',
    'https://fr.wikipedia.org/wiki/Cuba': 'html/Cuba.html',
    'https://fr.wikipedia.org/wiki/Danemark': 'html/Danemark.html',
    'https://fr.wikipedia.org/wiki/Djibouti': 'html/Djibouti.html',
    'https://fr.wikipedia.org/wiki/R%C3%A9publique_dominicaine': 'html/R%C3%A9publique_dominicaine.html',
    'https://fr.wikipedia.org/wiki/Dominique_(pays)': 'html/Dominique_(pays).html',
    'https://fr.wikipedia.org/wiki/%C3%89gypte': 'html/%C3%89gypte.html',
    'https://fr.wikipedia.org/wiki/%C3%89mirats_arabes_unis': 'html/%C3%89mirats_arabes_unis.html',
    'https://fr.wikipedia.org/wiki/%C3%89quateur_(pays)': 'html/%C3%89quateur_(pays).html',
    'https://fr.wikipedia.org/wiki/%C3%89rythr%C3%A9e': 'html/%C3%89rythr%C3%A9e.html',
    'https://fr.wikipedia.org/wiki/Espagne': 'html/Espagne.html',
    'https://fr.wikipedia.org/wiki/Estonie': 'html/Estonie.html',
    'https://fr.wikipedia.org/wiki/Eswatini': 'html/Eswatini.html',
    'https://fr.wikipedia.org/wiki/%C3%89tats-Unis': 'html/%C3%89tats-Unis.html',
    'https://fr.wikipedia.org/wiki/%C3%89thiopie': 'html/%C3%89thiopie.html',
    'https://fr.wikipedia.org/wiki/Fidji': 'html/Fidji.html',
    'https://fr.wikipedia.org/wiki/Finlande': 'html/Finlande.html',
    'https://fr.wikipedia.org/wiki/France': 'html/France.html',
    'https://fr.wikipedia.org/wiki/Gabon': 'html/Gabon.html',
    'https://fr.wikipedia.org/wiki/Gambie': 'html/Gambie.html',
    'https://fr.wikipedia.org/wiki/G%C3%A9orgie_(pays)': 'html/G%C3%A9orgie_(pays).html',
    'https://fr.wikipedia.org/wiki/Ghana': 'html/Ghana.html',
    'https://fr.wikipedia.org/wiki/Gr%C3%A8ce': 'html/Gr%C3%A8ce.html',
    'https://fr.wikipedia.org/wiki/Grenade_(pays)': 'html/Grenade_(pays).html',
    'https://fr.wikipedia.org/wiki/Guatemala': 'html/Guatemala.html',
    'https://fr.wikipedia.org/wiki/Guin%C3%A9e': 'html/Guin%C3%A9e.html',
    'https://fr.wikipedia.org/wiki/Guin%C3%A9e-Bissau': 'html/Guin%C3%A9e-Bissau.html',
    'https://fr.wikipedia.org/wiki/Guin%C3%A9e_%C3%A9quatoriale': 'html/Guin%C3%A9e_%C3%A9quatoriale.html',
    'https://fr.wikipedia.org/wiki/Guyana': 'html/Guyana.html',
    'https://fr.wikipedia.org/wiki/Ha%C3%AFti': 'html/Ha%C3%AFti.html',
    'https://fr.wikipedia.org/wiki/Honduras': 'html/Honduras.html',
    'https://fr.wikipedia.org/wiki/Hongrie': 'html/Hongrie.html',
    'https://fr.wikipedia.org/wiki/Inde': 'html/Inde.html',
    'https://fr.wikipedia.org/wiki/Indon%C3%A9sie': 'html/Indon%C3%A9sie.html',
    'https://fr.wikipedia.org/wiki/Irak': 'html/Irak.html',
    'https://fr.wikipedia.org/wiki/Iran': 'html/Iran.html',
    'https://fr.wikipedia.org/wiki/Irlande_(pays)': 'html/Irlande_(pays).html',
    'https://fr.wikipedia.org/wiki/Islande': 'html/Islande.html',
    'https://fr.wikipedia.org/wiki/Isra%C3%ABl': 'html/Isra%C3%ABl.html',
    'https://fr.wikipedia.org/wiki/Italie': 'html/Italie.html',
    'https://fr.wikipedia.org/wiki/Jama%C3%AFque': 'html/Jama%C3%AFque.html',
    'https://fr.wikipedia.org/wiki/Japon': 'html/Japon.html',
    'https://fr.wikipedia.org/wiki/Jordanie': 'html/Jordanie.html',
    'https://fr.wikipedia.org/wiki/Kazakhstan': 'html/Kazakhstan.html',
    'https://fr.wikipedia.org/wiki/Kenya': 'html/Kenya.html',
    'https://fr.wikipedia.org/wiki/Kirghizie': 'html/Kirghizie.html',
    'https://fr.wikipedia.org/wiki/Kiribati': 'html/Kiribati.html',
    'https://fr.wikipedia.org/wiki/Kowe%C3%AFt': 'html/Kowe%C3%AFt.html',
    'https://fr.wikipedia.org/wiki/Laos': 'html/Laos.html',
    'https://fr.wikipedia.org/wiki/Lesotho': 'html/Lesotho.html',
    'https://fr.wikipedia.org/wiki/Lettonie': 'html/Lettonie.html',
    'https://fr.wikipedia.org/wiki/Liban': 'html/Liban.html',
    'https://fr.wikipedia.org/wiki/Lib%C3%A9ria': 'html/Lib%C3%A9ria.html',
    'https://fr.wikipedia.org/wiki/Libye': 'html/Libye.html',
    'https://fr.wikipedia.org/wiki/Liechtenstein': 'html/Liechtenstein.html',
    'https://fr.wikipedia.org/wiki/Lituanie': 'html/Lituanie.html',
    'https://fr.wikipedia.org/wiki/Luxembourg': 'html/Luxembourg.html',
    'https://fr.wikipedia.org/wiki/Mac%C3%A9doine_du_Nord': 'html/Mac%C3%A9doine_du_Nord.html',
    'https://fr.wikipedia.org/wiki/Madagascar': 'html/Madagascar.html',
    'https://fr.wikipedia.org/wiki/Malaisie': 'html/Malaisie.html',
    'https://fr.wikipedia.org/wiki/Malawi': 'html/Malawi.html',
    'https://fr.wikipedia.org/wiki/Maldives': 'html/Maldives.html',
    'https://fr.wikipedia.org/wiki/Mali': 'html/Mali.html',
    'https://fr.wikipedia.org/wiki/Malte': 'html/Malte.html',
    'https://fr.wikipedia.org/wiki/Maroc': 'html/Maroc.html',
    'https://fr.wikipedia.org/wiki/%C3%8Eles_Marshall': 'html/%C3%8Eles_Marshall.html',
    'https://fr.wikipedia.org/wiki/Maurice_(pays)': 'html/Maurice_(pays).html',
    'https://fr.wikipedia.org/wiki/Mauritanie': 'html/Mauritanie.html',
    'https://fr.wikipedia.org/wiki/Mexique': 'html/Mexique.html',
    'https://fr.wikipedia.org/wiki/Micron%C3%A9sie_(pays)': 'html/Micron%C3%A9sie_(pays).html',
    'https://fr.wikipedia.org/wiki/Moldavie': 'html/Moldavie.html',
    'https://fr.wikipedia.org/wiki/Monaco': 'html/Monaco.html',
    'https://fr.wikipedia.org/wiki/Mongolie': 'html/Mongolie.html',
    'https://fr.wikipedia.org/wiki/Mont%C3%A9n%C3%A9gro': 'html/Mont%C3%A9n%C3%A9gro.html',
    'https://fr.wikipedia.org/wiki/Mozambique': 'html/Mozambique.html',
    'https://fr.wikipedia.org/wiki/Namibie': 'html/Namibie.html',
    'https://fr.wikipedia.org/wiki/Nauru': 'html/Nauru.html',
    'https://fr.wikipedia.org/wiki/N%C3%A9pal': 'html/N%C3%A9pal.html',
    'https://fr.wikipedia.org/wiki/Nicaragua': 'html/Nicaragua.html',
    'https://fr.wikipedia.org/wiki/Niger': 'html/Niger.html',
    'https://fr.wikipedia.org/wiki/Nig%C3%A9ria': 'html/Nig%C3%A9ria.html',
    'https://fr.wikipedia.org/wiki/Niue': 'html/Niue.html',
    'https://fr.wikipedia.org/wiki/Norv%C3%A8ge': 'html/Norv%C3%A8ge.html',
    'https://fr.wikipedia.org/wiki/Nouvelle-Z%C3%A9lande': 'html/Nouvelle-Z%C3%A9lande.html',
    'https://fr.wikipedia.org/wiki/Oman': 'html/Oman.html',
    'https://fr.wikipedia.org/wiki/Ouganda': 'html/Ouganda.html',
    'https://fr.wikipedia.org/wiki/Ouzb%C3%A9kistan': 'html/Ouzb%C3%A9kistan.html',
    'https://fr.wikipedia.org/wiki/Pakistan': 'html/Pakistan.html',
    'https://fr.wikipedia.org/wiki/Palaos': 'html/Palaos.html',
    'https://fr.wikipedia.org/wiki/Palestine_(%C3%89tat)': 'html/Palestine_(%C3%89tat).html',
    'https://fr.wikipedia.org/wiki/Panama': 'html/Panama.html',
    'https://fr.wikipedia.org/wiki/Papouasie-Nouvelle-Guin%C3%A9e': 'html/Papouasie-Nouvelle-Guin%C3%A9e.html',
    'https://fr.wikipedia.org/wiki/Paraguay': 'html/Paraguay.html',
    'https://fr.wikipedia.org/wiki/Pays-Bas': 'html/Pays-Bas.html',
    'https://fr.wikipedia.org/wiki/P%C3%A9rou': 'html/P%C3%A9rou.html',
    'https://fr.wikipedia.org/wiki/Philippines': 'html/Philippines.html',
    'https://fr.wikipedia.org/wiki/Pologne': 'html/Pologne.html',
    'https://fr.wikipedia.org/wiki/Portugal': 'html/Portugal.html',
    'https://fr.wikipedia.org/wiki/Qatar': 'html/Qatar.html',
    'https://fr.wikipedia.org/wiki/Roumanie': 'html/Roumanie.html',
    'https://fr.wikipedia.org/wiki/Royaume-Uni': 'html/Royaume-Uni.html',
    'https://fr.wikipedia.org/wiki/Russie': 'html/Russie.html',
    'https://fr.wikipedia.org/wiki/Rwanda': 'html/Rwanda.html',
    'https://fr.wikipedia.org/wiki/Saint-Christophe-et-Ni%C3%A9v%C3%A8s': 'html/Saint-Christophe-et-Ni%C3%A9v%C3%A8s.html',
    'https://fr.wikipedia.org/wiki/Sainte-Lucie': 'html/Sainte-Lucie.html',
    'https://fr.wikipedia.org/wiki/Saint-Marin': 'html/Saint-Marin.html',
    'https://fr.wikipedia.org/wiki/Saint-Vincent-et-les_Grenadines': 'html/Saint-Vincent-et-les_Grenadines.html',
    'https://fr.wikipedia.org/wiki/%C3%8Eles_Salomon': 'html/%C3%8Eles_Salomon.html',
    'https://fr.wikipedia.org/wiki/Salvador': 'html/Salvador.html',
    'https://fr.wikipedia.org/wiki/Samoa': 'html/Samoa.html',
    'https://fr.wikipedia.org/wiki/Sao_Tom%C3%A9-et-Principe': 'html/Sao_Tom%C3%A9-et-Principe.html',
    'https://fr.wikipedia.org/wiki/S%C3%A9n%C3%A9gal': 'html/S%C3%A9n%C3%A9gal.html',
    'https://fr.wikipedia.org/wiki/Serbie': 'html/Serbie.html',
    'https://fr.wikipedia.org/wiki/Seychelles': 'html/Seychelles.html',
    'https://fr.wikipedia.org/wiki/Sierra_Leone': 'html/Sierra_Leone.html',
    'https://fr.wikipedia.org/wiki/Singapour': 'html/Singapour.html',
    'https://fr.wikipedia.org/wiki/Slovaquie': 'html/Slovaquie.html',
    'https://fr.wikipedia.org/wiki/Slov%C3%A9nie': 'html/Slov%C3%A9nie.html',
    'https://fr.wikipedia.org/wiki/Somalie': 'html/Somalie.html',
    'https://fr.wikipedia.org/wiki/Soudan': 'html/Soudan.html',
    'https://fr.wikipedia.org/wiki/Soudan_du_Sud': 'html/Soudan_du_Sud.html',
    'https://fr.wikipedia.org/wiki/Sri_Lanka': 'html/Sri_Lanka.html',
    'https://fr.wikipedia.org/wiki/Su%C3%A8de': 'html/Su%C3%A8de.html',
    'https://fr.wikipedia.org/wiki/Suisse': 'html/Suisse.html',
    'https://fr.wikipedia.org/wiki/Suriname': 'html/Suriname.html',
    'https://fr.wikipedia.org/wiki/Syrie': 'html/Syrie.html',
    'https://fr.wikipedia.org/wiki/Tadjikistan': 'html/Tadjikistan.html',
    'https://fr.wikipedia.org/wiki/Tanzanie': 'html/Tanzanie.html',
    'https://fr.wikipedia.org/wiki/Tchad': 'html/Tchad.html',
    'https://fr.wikipedia.org/wiki/Tch%C3%A9quie': 'html/Tch%C3%A9quie.html',
    'https://fr.wikipedia.org/wiki/Tha%C3%AFlande': 'html/Tha%C3%AFlande.html',
    'https://fr.wikipedia.org/wiki/Timor_oriental': 'html/Timor_oriental.html',
    'https://fr.wikipedia.org/wiki/Togo': 'html/Togo.html',
    'https://fr.wikipedia.org/wiki/Tonga': 'html/Tonga.html',
    'https://fr.wikipedia.org/wiki/Trinit%C3%A9-et-Tobago': 'html/Trinit%C3%A9-et-Tobago.html',
    'https://fr.wikipedia.org/wiki/Tunisie': 'html/Tunisie.html',
    'https://fr.wikipedia.org/wiki/Turkm%C3%A9nistan': 'html/Turkm%C3%A9nistan.html',
    'https://fr.wikipedia.org/wiki/Turquie': 'html/Turquie.html',
    'https://fr.wikipedia.org/wiki/Tuvalu': 'html/Tuvalu.html',
    'https://fr.wikipedia.org/wiki/Ukraine': 'html/Ukraine.html',
    'https://fr.wikipedia.org/wiki/Uruguay': 'html/Uruguay.html',
    'https://fr.wikipedia.org/wiki/Vanuatu': 'html/Vanuatu.html',
    'https://fr.wikipedia.org/wiki/Vatican': 'html/Vatican.html',
    'https://fr.wikipedia.org/wiki/Venezuela': 'html/Venezuela.html',
    'https://fr.wikipedia.org/wiki/Vi%C3%AAt_Nam': 'html/Vi%C3%AAt_Nam.html',
    'https://fr.wikipedia.org/wiki/Y%C3%A9men': 'html/Y%C3%A9men.html',
    'https://fr.wikipedia.org/wiki/Zambie': 'html/Zambie.html',
    'https://fr.wikipedia.org/wiki/Zimbabwe': 'html/Zimbabwe.html'
}