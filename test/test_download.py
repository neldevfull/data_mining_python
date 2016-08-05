# coding: utf-8

import unittest
from unittest import mock
from download_data import download_length, download


BUFF_SIZE = 1024

class DownloadTest(unittest.TestCase):
    def test_download_with_known_length(self):
        response = mock.MagicMock()
        response.read = mock.MagicMock(side_effect=['Data'] * 2)

        output = mock.MagicMock()
        download_length(response, output, 1025)

        calls = [mock.call(BUFF_SIZE), mock.call(BUFF_SIZE)]
        response.read.assert_has_calls(calls)

        calls = [mock.call('Data'), mock.call('Data')]
        output.write.assert_has_calls(calls)

    def test_download_with_no_length(self):
        response = mock.MagicMock()
        response.read = mock.MagicMock(
            side_effect=['data', 'more data', '']
        )

        output = mock.MagicMock()
        output.write = mock.MagicMock()

        download(response, output)

        calls = [
            mock.call(BUFF_SIZE),
            mock.call(BUFF_SIZE),
            mock.call(BUFF_SIZE)
        ]
        response.read.assert_has_calls(calls)

        calls = [mock.call('data'), mock.call('more data')]
        output.write.assert_has_calls(calls)