import pytest


from neko_socket import Dispatcher


class TestDispatcher:

        
    @classmethod
    def setup_class(cls):
        cls.dp = Dispatcher()
       

    def test_callback_same_data(self):
        test_data = ("1", "TestData", "123123")
        gotted_data = []

        @self.dp.bind_event("test_callback", 1)
        def local_callback_foo(*data):
            nonlocal gotted_data
            gotted_data = data

        self.dp.execute_event(1, test_data)
        assert test_data == gotted_data

    def test_bind_same_id_callback(self):

        with pytest.raises(ValueError):
            @self.dp.bind_event("test_callback", 1)
            def local_callback_foo(*data):
                ...

    def test_bad_bind_args(self):
        with pytest.raises(TypeError):
            @self.dp.bind_event(1, 2)
            def local_callback_foo(*data):
                ...

        with pytest.raises(TypeError):
            @self.dp.bind_event("d", "")
            def local_callback_foo(*data):
                ...

        with pytest.raises(TypeError):
            self.dp.add_event("", "a", 2)



