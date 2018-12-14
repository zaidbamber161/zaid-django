from django.test import TestCase
from .models import MyNotes
import datetime
from django.http import HttpRequest
from django.utils import timezone
from . import views


class NotesModelTests(TestCase):

    def setUpNotes(self):
        MyNotes.objects.create(title='my note test', description='the task is lengthy',
                               note_created_date='2018-12-17')

    def test_get_Notes(self):
        note = MyNotes.objects.get(id=1)
        self.assertEqual(note.title(), 'my note test')


class HomePageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)


class NoteCrudTests(TestCase):

    def setUp(self):
        first_note = MyNotes()
        first_note.title = 'The first note'
        first_note.description = 'this note is created by Zaid'
        first_note.note_created_date = '2018-12-17'
        first_note.save()
        second_note = MyNotes()
        second_note.title = 'The second note'
        second_note.description = 'this note is created by Bamber'
        second_note.note_created_date = '2018-11-17'
        second_note.save()

        return super(NoteCrudTests, self).setUp()

    def test_add_Note(self):
        saved_items = MyNotes.objects.all()
        self.assertEqual(saved_items.count(), 2)

    def test_update_Note(self):
        expected_total_notes = MyNotes.objects.all()
        self.assertEqual(expected_total_notes.count(), 2)
        note = MyNotes.objects.get(id=1)
        note.title = 'The updated note'
        note.description = 'this note is created by Zee'
        note.note_created_date = '2018-12-01'
        note.save()
        updated_items = MyNotes.objects.get(id=1)
        self.assertEqual(updated_items.title, 'The updated note')

    def test_delete_Note(self):
        note1 = MyNotes.objects.get(id=1)
        note2 = MyNotes.objects.get(id=2)
        note1.delete()
        note2.delete()
        expected_total_notes = MyNotes.objects.all()
        self.assertEqual(expected_total_notes.count(), 2)
