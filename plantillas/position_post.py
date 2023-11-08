import squema

def template_position(input:squema.Position):
    function_str = []
    for func in input.functions.split("|"):
        func = f"- {func}\n"
        function_str.append(func)
    function_str = " ".join(function_str)

    requirements_str = []
    for req in input.requirements.split("|"):
        req = f"- {req}\n"
        function_str.append(req)
    requirements_str = " ".join(requirements_str)
        
    template = f"""
{input.name}
SuperLearner es una ONG sin fines de lucro enfocado en el desarrollo de programas sociales sostenibles que promuevan el desarrollo integral, contribuyan a la mejorar calidad de vida y oportunidades de los niños, niñas, adolescentes y jóvenes de comunidades vulnerables.

Estamos en busca de individuos proactivos, con un fuerte espíritu de servicio y el deseo de contribuir a la mejora de la sociedad, especialmente en las comunidades más vulnerables. ¿Listo para marcar la diferencia? Únete a Superlearner y forma parte del cambio.

Más sobre nosotros
- Sitio web: superlearnerperu.com
- Instagram : @superlearnerperu
- Facebook : @SuperlearnerPeru
- YouTube: @superlearnerperu880

Funciones:
{function_str}

Requirements:
{requirements_str}
"""