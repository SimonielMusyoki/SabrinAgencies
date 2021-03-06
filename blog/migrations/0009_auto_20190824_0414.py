# Generated by Django 2.2.3 on 2019-08-24 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190823_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDate', models.DateTimeField(auto_now_add=True)),
                ('EndDate', models.DateTimeField(help_text='End date')),
                ('Active', models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3)),
                ('Rent', models.DecimalField(decimal_places=2, help_text='The rent to this unit', max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PropertyName', models.CharField(help_text='The Name of the property', max_length=255)),
                ('Address', models.CharField(help_text='The address of the above property', max_length=255)),
                ('City', models.CharField(help_text='The city where the property is located', max_length=255)),
                ('County', models.CharField(help_text='The county of the city above', max_length=100)),
                ('Picture1', models.ImageField(help_text='Attach first image of your property', upload_to='')),
                ('Picture2', models.ImageField(blank=True, help_text='Attach second image of your property', null=True, upload_to='')),
                ('Picture3', models.ImageField(blank=True, help_text='Attach third image of your property', null=True, upload_to='')),
                ('Picture4', models.ImageField(blank=True, help_text='Attach fourth image of your property', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(help_text='First name', max_length=100)),
                ('LastName', models.CharField(help_text='Last name', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UnitNumber', models.CharField(max_length=255, unique=True)),
                ('PropertyID', models.CharField(help_text='The property number where this unit exists', max_length=255)),
                ('Floor', models.IntegerField(help_text='The floor of the unit')),
                ('Bedrooms', models.IntegerField(help_text='Number of bedrooms in the units')),
                ('Bathrooms', models.IntegerField(help_text='Number of bathrooms the unit has')),
                ('Status', models.CharField(choices=[('vacant', 'VACANT'), ('occupied', 'OCCUPIED'), ('closed', 'CLOSED')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VendorName', models.CharField(help_text='Enter the vendo name', max_length=255)),
                ('Phone', models.CharField(help_text='Phone number of the vendor', max_length=255)),
                ('ContactPerson', models.CharField(max_length=255)),
                ('Email', models.EmailField(help_text='Email address', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaymentAmount', models.DecimalField(decimal_places=2, help_text='Amount of Money Paid', max_digits=9)),
                ('PaymentDate', models.DateTimeField(auto_now_add=True)),
                ('LeaseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Lease')),
                ('UnitID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Units')),
            ],
        ),
        migrations.AddField(
            model_name='lease',
            name='PropertyID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Properties'),
        ),
        migrations.AddField(
            model_name='lease',
            name='TenantID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Tenant'),
        ),
        migrations.AddField(
            model_name='lease',
            name='UnitID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Units'),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(choices=[('plumbing', 'Plumping'), ('electrical', 'Electrical'), ('repair and mantinence', 'Repair and Maintenance')], max_length=255)),
                ('Cost', models.DecimalField(decimal_places=2, max_digits=9)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Reciept', models.FileField(help_text='Picture of the receipt', upload_to='media/Receipts/')),
                ('isPaid', models.BooleanField(default=True)),
                ('PropertyID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Properties')),
                ('UnitID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Units')),
                ('VendorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Vendor')),
            ],
        ),
    ]
