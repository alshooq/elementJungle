from flask import request
from typing import Dict

class DataView:
    __dict__: Dict[str, Dict[str, Dict[str, str]]]

    def __init__(self) -> None:
        """
        Initialize the DataView class.

        This class contains the data of the Nickel, Palladium, Platinum and Darmstadtium elements.
        The data is stored in a dictionary, with the key being the element name and the value being a dictionary with the element data.
        The element data is stored in a dictionary, with the key being the page name and the value being a dictionary with the page data.
        The page data is stored in a dictionary, with the key being the page section name and the value being the page section data.
        The page section data is stored in a dictionary, with the key being the page section item name and the value being the page section item data.

        :ivar nickel: A dictionary with the Nickel element data.
        :type nickel: Dict[str, Dict[str, Union[int, float, str]]]
        :ivar palladium: A dictionary with the Palladium element data.
        :type palladium: Dict[str, Dict[str, Union[int, float, str]]]
        :ivar platinum: A dictionary with the Platinum element data.
        :type platinum: Dict[str, Dict[str, Union[int, float, str]]]
        :ivar darmstadtium: A dictionary with the Darmstadtium element data.
        :type darmstadtium: Dict[str, Dict[str, Union[int, float, str]]]
        """

        self.nickel = {
            "pagina1": {
                "Nome": "Níquel (Ni)",
                "Número Atômico": "28",
                "Peso Atômico": "58.693",
                "Categoria": "Metal de Transição",
                "Densidade (g/cm³)": "8.908",
                "Camada de Valência": "N"
            },
            "pagina2": {
                "Nome": "Níquel (Ni)",
                "Distribuição Eletrônica": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁸",
                "Números Quânticos (n, ℓ, mℓ, mₛ)": "3, 2 (d), 0, +½",
                "Detalhes": "Distribuição segue o diagrama de Pauling, onde a subcamada 4s é preenchida antes da 3d."
            },
            "pagina3": {
                "Nome": "Níquel (Ni)",
                "Descrição": "Metal branco‑prateado com leve tom dourado, resistente à corrosão.",
                "Usos": "Moedas, ligas magnéticas, baterias recarregáveis, aço inoxidável.",
                "Descoberta": "Axel Fredrik Cronstedt em 1751.",
                "História": "Usado desde a China antiga, explorado amplamente no século 18.",
                "Fato Interessante": "5º elemento mais abundante na crosta terrestre."
            }
        }

        self.palladium = {
            "pagina1": {
                "Nome": "Paládio (Pd)",
                "Número Atômico": "46",
                "Peso Atômico": "106.420",
                "Categoria": "Metal de Transição",
                "Densidade (g/cm³)": "12.023",
                "Camada de Valência": "N"
            },
            "pagina2": {
                "Nome": "Paládio (Pd)",
                "Distribuição Eletrônica": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 4d¹⁰",
                "Números Quânticos (n, ℓ, mℓ, mₛ)": "4, 2 (d), 2, +½",
                "Detalhes": "O paládio não segue a ordem esperada de preenchimento, com a subcamada 4d sendo preenchida antes da 5s, devido à estabilidade da subcamada d.",
            },
            "pagina3": {
                "Nome": "Paládio (Pd)",
                "Descrição": "Metal branco-prateado, maleável, raro e excelente catalisador.",
                "Usos": "Catalisadores automotivos, joias, eletrônicos.",
                "Descoberta": "William Hyde Wollaston em 1803.",
                "História": "Nomeado em homenagem ao asteroide Pallas.",
                "Fato Interessante": "Absorve hidrogênio até 900 vezes seu volume."
            }
        }

        self.platinum = {
            "pagina1": {
                "Nome": "Platina (Pt)",
                "Número Atômico": "78",
                "Peso Atômico": "195.084",
                "Categoria": "Metal de Transição",
                "Densidade (g/cm³)": "21.45",
                "Camada de Valência": "P"
            },
            "pagina2": {
                "Nome": "Platina (Pt)",
                "Distribuição Eletrônica": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s¹ 5d⁹",
                "Números Quânticos (n, ℓ, mℓ, mₛ)": "5, 2 (d), 1, +½",
                "Detalhes": "Desvio da ordem esperada devido à estabilidade da subcamada d como no Paládio."
            },
            "pagina3": {
                "Nome": "Platina (Pt)",
                "Descrição": "Metal denso, maleável, resistente à corrosão e valioso.",
                "Usos": "Joias, catalisadores, equipamentos médicos e de laboratório.",
                "Descoberta": "Antonio de Ulloa em 1735.",
                "História": "Utilizado por povos pré-colombianos na América do Sul.",
                "Fato Interessante": "Mais raro que ouro e altamente valorizado."
            }
        }

        self.darmstadtium = {
            "pagina1": {
                "Nome": "Darmstádio (Ds)",
                "Número Atômico": "110",
                "Peso Atômico": "281.000",
                "Categoria": "Metal de Transição (sintético)",
                "Densidade": "Desconhecida",
                "Camada de Valência": "Q"
            },
            "pagina2": {
                "Nome": "Darmstádio (Ds)",
                "Distribuição Eletrônica": "1s² … 7s² 5f¹⁴ 6d⁸",
                "Número Quânticos (n, ℓ, mℓ, mₛ)": "6, 2 (d), 0, +½",
                "Detalhes": "Não se sabe ao exato sua distribuição eletrônica mas espera-se que sua distribuição não siga o diagrama de Linus Pauling como seus antecessores na Família."
            },
            "pagina3": {
                "Nome": "Darmstádio (Ds)",
                "Descrição": "Elemento sintético, altamente instável e radioativo.",
                "Usos": "Sem aplicações práticas; usado apenas em pesquisa nuclear.",
                "Descoberta": "Instituto GSI Helmholtz, Alemanha (1994).",
                "História": "Nomeado em homenagem à cidade de Darmstadt.",
                "Fato Interessante": "Produzido em aceleradores em quantidades atômicas."
            }
        }
        
def data():
    """
    Endpoint to get data for a specific element and page.
    
    :param element: The id of the element (0-8)
    :type element: int
    :param page: The page of the element (1-3)
    :type page: int
    :return: The data for the element and page
    :rtype: dict
    :raises: 404 if the element or page doesn't exist
    :raises: 500 if there is an internal server error
    """
    
    data_view = DataView()
    
    try:
        content = request.get_json()
        element_id = int(content.get('element'))
        page = int(content.get('page'))
        
        data_ = data_view.__dict__.get(
            
            list(data_view.__dict__.keys())[element_id], {}
            
        ).get(
            
            f'pagina{page}', {}
            
        )

        if not data_:
            return {"error": 404}

        return data_

    except Exception:
        
        return {"error": 500}
