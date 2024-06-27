from django.shortcuts import render
from datetime import date

# Create your views here.
all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Pablo",
        "date": date(2024, 6, 26),
        "title": "Montain hiking!",
        "excerpt": "Com estas tabelas e scripts, você terá um banco de dados SQL que pode ser usado para gerenciar a agenda",
        "content": """Com estas tabelas e scripts, você terá um banco de dados SQL que pode ser usado para gerenciar a agenda de marcações de clientes.
          Certifique-se de ajustar os scripts conforme necessário para se adequar ao seu ambiente e requisitos específicos."""
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Pablo",
        "date": date(2024, 6, 26),
        "title": "Programmin is great!",
        "excerpt": "Desvendando o Mundo da Programação: Um Guia para Iniciantes",
        "content": """Neste post, mergulhamos no fascinante universo da programação. Se você sempre quis entender como os aplicativos e sites que usamos diariamente são criados, 
        este guia é para você. Vamos explorar os conceitos básicos, as linguagens de programação mais populares e fornecer dicas valiosas para quem está começando nessa jornada. 
        Descubra os segredos por trás do código e dê os primeiros passos para se tornar um desenvolvedor habilidoso.
        Venha aprender e se inspirar com histórias de sucesso e recursos gratuitos que irão impulsionar sua carreira na tecnologia."""
    },
    {
        "slug": "see-florest",
        "image": "woods.jpg",
        "author": "Pablo",
        "date": date(2024, 6, 26),
        "title": "See all the forest",
        "excerpt": "A Magia das Florestas: Importância, Conservação e Curiosidades",
        "content": """As florestas são muito mais do que apenas um conjunto de árvores; elas são ecossistemas vitais que sustentam a vida na Terra. 
        Neste post, exploramos a importância das florestas para a biodiversidade, o clima e a economia. Discutimos os desafios da conservação, as ameaças enfrentadas por esses ecossistemas
        e as iniciativas globais para protegê-los. Além disso, compartilhamos curiosidades fascinantes sobre algumas das florestas mais icônicas do mundo. 
        Junte-se a nós nesta jornada verde e descubra como podemos contribuir para preservar esses pulmões do planeta para as futuras gerações."""
    }
]

def get_date(post):
    return post["date"]


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_post = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_post
    })


def post(request):
    return render (request, "blog/all-posts.html", {
        "posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    print(identified_post)
    return render (request, "blog/post-detail.html", {
        "posts": identified_post
        })




