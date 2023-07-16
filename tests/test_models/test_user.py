#!/usr/bin/python3
"""Defines unittests for models/user.py."""

import unittest
from datetime import datetime
import os
from time import sleep

from models.user import User
import models


class TestUserInstantiation(unittest.TestCase):
    """Test cases for User instantiation."""

    def test_no_args_instantiates(self):
        user = User()
        self.assertEqual(User, type(user))

    def test_new_instance_stored_in_objects(self):
        user = User()
        self.assertIn(user, models.storage.all().values())

    def test_id_is_public_str(self):
        user = User()
        self.assertEqual(str, type(user.id))

    def test_created_at_is_public_datetime(self):
        user = User()
        self.assertEqual(datetime, type(user.created_at))

    def test_updated_at_is_public_datetime(self):
        user = User()
        self.assertEqual(datetime, type(user.updated_at))

    def test_email_is_public_class_attribute(self):
        user = User()
        self.assertEqual(str, type(User.email))
        self.assertIn("email", dir(user))
        self.assertNotIn("email", user.__dict__)

    def test_password_is_public_class_attribute(self):
        user = User()
        self.assertEqual(str, type(User.password))
        self.assertIn("password", dir(user))
        self.assertNotIn("password", user.__dict__)

    def test_first_name_is_public_class_attribute(self):
        user = User()
        self.assertEqual(str, type(User.first_name))
        self.assertIn("first_name", dir(user))
        self.assertNotIn("first_name", user.__dict__)

    def test_last_name_is_public_class_attribute(self):
        user = User()
        self.assertEqual(str, type(User.last_name))
        self.assertIn("last_name", dir(user))
        self.assertNotIn("last_name", user.__dict__)

    def test_two_users_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_two_users_different_created_at(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_two_users_different_updated_at(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        user_str = user.__str__()
        self.assertIn("[User] (123456)", user_str)
        self.assertIn("'id': '123456'", user_str)
        self.assertIn("'created_at': " + dt_repr, user_str)
        self.assertIn("'updated_at': " + dt_repr, user_str)

    def test_args_unused(self):
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        user = User(
            id="345",
            created_at=dt_iso,
            updated_at=dt_iso,
            email="test@example.com",
            password="password",
            first_name="John",
            last_name="Doe",
        )
        self.assertEqual(user.id, "345")
        self.assertEqual(user.created_at, dt)
        self.assertEqual(user.updated_at, dt)
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(
                id=None,
                created_at=None,
                updated_at=None,
                email=None,
                password=None,
                first_name=None,
                last_name=None,
            )


class TestUserSave(unittest.TestCase):
    """Test cases for User save method."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        self.assertLess(first_updated_at, user.updated_at)

    def test_two_saves(self):
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        second_updated_at = user.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        user.save()
        self.assertLess(second_updated_at, user.updated_at)

    def test_save_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_updates_file(self):
        user = User()
        user.save()
        user_id = "User." + user.id
        with open("file.json", "r") as f:
            self.assertIn(user_id, f.read())


class TestUserToDict(unittest.TestCase):
    """Test cases for User to_dict method."""

    def test_to_dict_type(self):
        user = User()
        self.assertTrue(dict, type(user.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())
        self.assertIn("email", user.to_dict())
        self.assertIn("password", user.to_dict())
        self.assertIn("first_name", user.to_dict())
        self.assertIn("last_name", user.to_dict())

    def test_to_dict_contains_added_attributes(self):
        user = User()
        user.age = 25
        user.my_number = 98
        self.assertEqual(25, user.age)
        self.assertIn("my_number", user.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        user.email = "test@example.com"
        user.password = "password"
        user.first_name = "John"
        user.last_name = "Doe"
        tdict = {
            "id": "123456",
            "__class__": "User",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
            "email": "test@example.com",
            "password": "password",
            "first_name": "John",
            "last_name": "Doe",
        }
        self.assertDictEqual(user.to_dict(), tdict)

    def test_to_dict_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)


class TestUserCreate(unittest.TestCase):
    """Test cases for User create method."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.create(None)

    def test_create_creates_user_instance(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.create()
        user_id = "User." + user.id
        self.assertIn(user_id, models.storage.all())
        new_user = models.storage.all()[user_id]
        self.assertEqual(user.email, new_user.email)
        self.assertEqual(user.password, new_user.password)

    def test_create_updates_file(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.create()
        user_id = "User." + user.id
        with open("file.json", "r") as f:
            self.assertIn(user_id, f.read())

    def test_create_twice_same_id(self):
        user1 = User()
        user1.create()
        user2 = User()
        user2.create()
        self.assertEqual(user1.id, user2.id)

    def test_create_with_already_created_user(self):
        user = User()
        user.create()
        with self.assertRaises(AttributeError):
            user.create()

    def test_create_with_no_email_attribute(self):
        user = User()
        with self.assertRaises(AttributeError):
            user.create()

    def test_create_with_no_password_attribute(self):
        user = User()
        user.email = "test@example.com"
        with self.assertRaises(AttributeError):
            user.create()

    def test_create_with_existing_email(self):
        user1 = User()
        user1.email = "test@example.com"
        user1.password = "password"
        user1.create()
        user2 = User()
        user2.email = "test@example.com"
        user2.password = "123456"
        user2.create()
        self.assertEqual(user1.password, user2.password)


class TestUserDestroy(unittest.TestCase):
    """Test cases for User destroy method."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_destroy_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.destroy(None)

    def test_destroy_removes_user_instance(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.create()
        user_id = "User." + user.id
        self.assertIn(user_id, models.storage.all())
        user.destroy()
        self.assertNotIn(user_id, models.storage.all())

    def test_destroy_removes_user_instance_from_file(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.create()
        user_id = "User." + user.id
        with open("file.json", "r") as f:
            self.assertIn(user_id, f.read())
        user.destroy()
        with open("file.json", "r") as f:
            self.assertNotIn(user_id, f.read())

    def test_destroy_with_unsaved_user(self):
        user = User()
        with self.assertRaises(AttributeError):
            user.destroy()

    def test_destroy_with_nonexistent_user(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.create()
        user_id = "User." + user.id
        models.storage.all().pop(user_id)
        with self.assertRaises(KeyError):
            user.destroy()


class TestUserUpdate(unittest.TestCase):
    """Test cases for User update method."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_update_with_no_args(self):
        user = User()
        with self.assertRaises(TypeError):
            user.update()

    def test_update_with_kwargs(self):
        user = User()
        user.update(first_name="John", last_name="Doe")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_update_with_invalid_kwargs(self):
        user = User()
        user.update(first_name="John", invalid_key="value")
        self.assertEqual(user.first_name, "John")
        with self.assertRaises(AttributeError):
            user.invalid_key

    def test_update_with_None_kwargs(self):
        user = User()
        with self.assertRaises(TypeError):
            user.update(None)

    def test_update_with_existing_user(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.create()
        user_id = "User." + user.id
        old_updated_at = user.updated_at
        sleep(0.05)
        user.update(email="new@example.com")
        self.assertEqual(user.email, "new@example.com")
        self.assertEqual(user.updated_at, old_updated_at)
        with open("file.json", "r") as f:
            self.assertIn(user_id, f.read())


class TestUserAll(unittest.TestCase):
    """Test cases for User all method."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_all_returns_dict(self):
        users = User.all()
        self.assertTrue(dict, type(users))

    def test_all_returns_dict_of_users(self):
        user1 = User()
        user1.create()
        user2 = User()
        user2.create()
        users = User.all()
        self.assertIn(user1, users.values())
        self.assertIn(user2, users.values())

    def test_all_returns_empty_dict(self):
        users = User.all()
        self.assertEqual(0, len(users))


class TestUserShow(unittest.TestCase):
    """Test cases for User show method."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_show_with_no_args(self):
        user = User()
        with self.assertRaises(TypeError):
            user.show()

    def test_show_with_id_kwarg(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.create()
        user_id = "User." + user.id
        with captured_output() as (out, err):
            user.show(id=user.id)
        output = out.getvalue().strip()
        self.assertIn(user_id, output)
        self.assertIn(user.email, output)
        self.assertIn(user.password, output)

    def test_show_with_invalid_id_kwarg(self):
        user = User()
        with self.assertRaises(AttributeError):
            user.show(id="invalid_id")

    def test_show_with_existing_user(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.create()
        user_id = "User." + user.id
        old_updated_at = user.updated_at
        sleep(0.05)
        user.show()
        self.assertEqual(user.updated_at, old_updated_at)
        with open("file.json", "r") as f:
            self.assertIn(user_id, f.read())

    def test_show_with_nonexistent_user(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.create()
        user_id = "User." + user.id
        models.storage.all().pop(user_id)
        with self.assertRaises(KeyError):
            user.show()


class TestUserUpdateCommand(unittest.TestCase):
    """Test cases for User update command."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_update_command_with_no_args(self):
        user = User()
        with self.assertRaises(TypeError):
            user.do_update(None)

    def test_update_command_with_no_id_kwarg(self):
        user = User()
        with self.assertRaises(AttributeError):
            user.do_update("User")

    def test_update_command_with_no_update_kwargs(self):
        user = User()
        with self.assertRaises(AttributeError):
            user.do_update("User " + user.id)

    def test_update_command_with_invalid_kwargs(self):
        user = User()
        user.create()
        user_id = "User." + user.id
        with captured_output() as (out, err):
            user.do_update("User " + user.id + " invalid_key value")
        output = out.getvalue().strip()
        self.assertIn(user_id, output)
        self.assertNotIn("invalid_key", output)
        with self.assertRaises(AttributeError):
            user.invalid_key

    def test_update_command_with_existing_user(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.create()
        user_id = "User." + user.id
        old_updated_at = user.updated_at
        sleep(0.05)
        with captured_output() as (out, err):
            user.do_update("User " + user.id + " email new@example.com")
        output = out.getvalue().strip()
        self.assertIn(user_id, output)
        self.assertIn("new@example.com", output)
        self.assertNotIn("password", output)
        self.assertEqual(user.updated_at, old_updated_at)
        with open("file.json", "r") as f:
            self.assertIn(user_id, f.read())

    def test_update_command_with_nonexistent_user(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.create()
        user_id = "User." + user.id
        models.storage.all().pop(user_id)
        with self.assertRaises(KeyError):
            user.do_update("User " + user.id + " email new@example.com")


if __name__ == '__main__':
    unittest.main()
