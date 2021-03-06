# Generated by Django 4.0.6 on 2022-07-16 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_el', models.DateField(auto_now_add=True)),
                ('actualizado_el', models.DateField(auto_now=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_el', models.DateField(auto_now_add=True)),
                ('actualizado_el', models.DateField(auto_now=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_el', models.DateField(auto_now_add=True)),
                ('actualizado_el', models.DateField(auto_now=True)),
                ('zona', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_el', models.DateField(auto_now_add=True)),
                ('actualizado_el', models.DateField(auto_now=True)),
                ('codigo', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('stock', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.marca')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.ubicacion')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
