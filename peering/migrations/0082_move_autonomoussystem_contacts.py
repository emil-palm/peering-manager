# Generated by Django 3.2.9 on 2021-12-10 23:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("peering", "0081_alter_directpeeringsession_relationship"),
        ("messaging", "0001_initial"),
    ]

    def create_contacts(apps, schema_editor):
        db_alias = schema_editor.connection.alias
        AutonomousSystem = apps.get_model("peering.AutonomousSystem")
        ContactRole = apps.get_model("messaging.ContactRole")
        Contact = apps.get_model("messaging.Contact")
        ContactAssignment = apps.get_model("messaging.ContactAssignment")
        ContentType = apps.get_model("contenttypes", "ContentType")
        AutonomousSystemType = ContentType.objects.get(
            model=AutonomousSystem._meta.model_name,
            app_label=AutonomousSystem._meta.app_label,
        )

        # Create a placeholder role
        role = ContactRole.objects.using(db_alias).create(name="FIXME", slug="fixme")
        # Get AS with a contact name set
        for asn in AutonomousSystem.objects.using(db_alias).exclude(
            contact_name__exact=""
        ):
            try:
                contact = Contact.objects.using(db_alias).get(name=asn.contact_name)
            except Contact.DoesNotExist:
                # Create a contact with the contact details of the AS
                contact = Contact.objects.using(db_alias).create(
                    name=asn.contact_name,
                    phone=asn.contact_phone,
                    email=asn.contact_email,
                )
            # Assign the contact to the AS with the placeholder role set
            ContactAssignment.objects.create(
                content_type=AutonomousSystemType,
                object_id=asn.pk,
                contact=contact,
                role=role,
            )

    operations = [
        migrations.RunPython(create_contacts),
        migrations.RemoveField(model_name="autonomoussystem", name="contact_email"),
        migrations.RemoveField(model_name="autonomoussystem", name="contact_name"),
        migrations.RemoveField(model_name="autonomoussystem", name="contact_phone"),
    ]
