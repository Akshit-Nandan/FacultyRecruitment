# Generated by Django 2.2.20 on 2021-04-26 06:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('application_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.datetime(2021, 4, 26, 6, 13, 49, 523290, tzinfo=utc))),
                ('post', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=20)),
                ('Research_Domain', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Teaching_and_research_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=200)),
                ('level', models.CharField(blank=True, choices=[('UG', 'Undergraduate'), ('PG', 'Postgraduate')], max_length=2, null=True)),
                ('sole_instructor', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, null=True)),
                ('developer_of_course', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, null=True)),
                ('name_of_student', models.CharField(max_length=200, null=True)),
                ('year_of_completion', models.IntegerField(blank=True, null=True)),
                ('name_of_institute', models.CharField(blank=True, max_length=200, null=True)),
                ('guide', models.CharField(blank=True, max_length=200, null=True)),
                ('organisation', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('co_investigators', models.CharField(blank=True, max_length=200, null=True)),
                ('period', models.CharField(blank=True, max_length=100, null=True)),
                ('name_of_body', models.CharField(blank=True, max_length=150, null=True)),
                ('status_of_membership', models.CharField(blank=True, max_length=150, null=True)),
                ('applicant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teaching_and_research_details', to='recruitment.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Seminar_Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.TextField()),
                ('seminar_subject', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('published', models.TextField()),
                ('duration', models.CharField(max_length=20)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seminar_articles', to='recruitment.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Research_Exp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=20)),
                ('to', models.CharField(max_length=20)),
                ('duration', models.CharField(max_length=20)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='research_exp', to='recruitment.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Professional_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('from_year', models.IntegerField()),
                ('to_year', models.IntegerField()),
                ('role', models.CharField(max_length=250)),
                ('pay_scale', models.IntegerField()),
                ('emoluments', models.IntegerField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professional_details', to='recruitment.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Other_important_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awards_and_recognition', models.TextField()),
                ('any_other_relevant_information', models.TextField()),
                ('reference', models.TextField()),
                ('statement_of_objective', models.TextField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_details', to='recruitment.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Newspaper_Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.TextField()),
                ('journal_name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('date_published', models.CharField(max_length=20)),
                ('referred', models.TextField()),
                ('level', models.CharField(max_length=20)),
                ('naas', models.TextField()),
                ('isbn_issn', models.TextField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newspaper_article', to='recruitment.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('chapter', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('date_of_publisher', models.CharField(max_length=100)),
                ('isbn_issn', models.TextField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant', to='recruitment.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('date_publish', models.CharField(max_length=20)),
                ('isbn', models.TextField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='recruitment.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Academic_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200)),
                ('area_of_qualification', models.CharField(max_length=200)),
                ('category_of_university', models.CharField(max_length=200)),
                ('institute', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('ResultAwaited', 'ResultAwaited'), ('FinalAwaited', 'FinalAwaited'), ('Ongoing', 'Ongoing')], max_length=200)),
                ('year_of_passing', models.IntegerField()),
                ('percentage', models.FloatField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_detail', to='recruitment.Applicant')),
            ],
        ),
    ]
