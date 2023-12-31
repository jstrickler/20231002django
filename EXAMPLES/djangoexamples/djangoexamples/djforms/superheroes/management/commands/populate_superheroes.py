import yaml
from django.core.management.base import BaseCommand
from superheroes.models import Superhero, Enemy, Power, City


class Command(BaseCommand):
    help = "Populates the superhero database"

    def handle(self, *args, **options):
        with open("../../../DATA/superheroes.yaml") as sup_in:
            sup_data = yaml.load(sup_in, Loader=yaml.BaseLoader)

        for s in sup_data:
            self.stdout.write(f"Adding {s['name']}")

            # add city
            city_name = s['city']
            results = City.objects.filter(name=city_name)
            if results:
                city = results[0]
            else:
                city = City(name=s['city'])
                city.save()

            # add powers
            powers = []
            for power, desc in s['powers']:
                results = Power.objects.filter(name=power)
                if results:
                    p = results[0]
                    powers.append(p)
                else:
                    p = Power(name=power, description=desc)
                    p.save()
                powers.append(p)

            # add enemies
            enemies = []
            for enemy in s['enemies']:
                results = Enemy.objects.filter(name=enemy)
                if not results:
                    e = Enemy(name=enemy)
                    e.save()
                    enemies.append(e)

            sup = Superhero(
                name=s['name'],
                real_name=s['real name'],
                secret_identity=s['secret identity'],
                city=city,
            )
            sup.save()
            for power in powers:
                sup.powers.add(power)

            for enemy in enemies:
                sup.enemies.add(enemy)
            sup.save()

            self.stdout.write(
                self.style.SUCCESS('Successfully populated superheroes')
            )
import yaml
from django.core.management.base import BaseCommand
from superheroes.models import Superhero, Enemy, Power, City


class Command(BaseCommand):
    help = "Populates the superhero database"

    def handle(self, *args, **options):
        with open("../../../DATA/superheroes.yaml") as sup_in:
            sup_data = yaml.load(sup_in, Loader=yaml.BaseLoader)

        for s in sup_data:
            self.stdout.write(f"Adding {s['name']}")

            # add city
            city_name = s['city']
            results = City.objects.filter(name=city_name)
            if results:
                city = results[0]
            else:
                city = City(name=s['city'])
                city.save()

            # add powers
            powers = []
            for power, desc in s['powers']:
                results = Power.objects.filter(name=power)
                if results:
                    p = results[0]
                    powers.append(p)
                else:
                    p = Power(name=power, description=desc)
                    p.save()
                powers.append(p)

            # add enemies
            enemies = []
            for enemy in s['enemies']:
                results = Enemy.objects.filter(name=enemy)
                if not results:
                    e = Enemy(name=enemy)
                    e.save()
                    enemies.append(e)

            sup = Superhero(
                name=s['name'],
                real_name=s['real name'],
                secret_identity=s['secret identity'],
                city=city,
            )
            sup.save()
            for power in powers:
                sup.powers.add(power)

            for enemy in enemies:
                sup.enemies.add(enemy)
            sup.save()

            self.stdout.write(
                self.style.SUCCESS('Successfully populated superheroes')
            )
