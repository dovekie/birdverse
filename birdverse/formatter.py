import json

# 'common_name', 'family_name', 'genus_name', 'id', 'order_name', 'species_name', 'spuh'

def create_dto(birds):
    dto = []
    for bird in birds:
        bird_obj = {'id': bird.id,
                    'common_name': bird.common_name,
                    'family_name': bird.family_name,
                    'species_name': bird.species_name,
                    'order_name': bird.order_name,
                    'spuh': bird.spuh
                    }
        dto.append(bird_obj)
    return dto