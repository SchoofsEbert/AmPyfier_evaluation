import os
import shutil
import unittest
from twelve_tone.midi import MIDIFile


class TestMIDIFile(unittest.TestCase):

    def test_init(self):
        m = MIDIFile()
        self.assertEquals(m.step_counter, 0)
        m = MIDIFile(filename='test.mid')
        self.assertEquals(m.filename, 'test.mid')

    def test_create(self):
        notes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        path = 'tmp'
        os.makedirs(path, exist_ok=True)
        os.chdir(path)
        m = MIDIFile(filename='test.mid')
        m.create(notes)
        self.assertTrue(os.path.exists(os.path.join(os.getcwd(), 'test.mid')))
        os.chdir(os.pardir)
        shutil.rmtree('tmp', ignore_errors=True)

    def test_create_amp(self):
        notes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        path = 'tmp'
        os.makedirs(path, exist_ok=True)
        os.chdir(path)
        m = MIDIFile(filename='test.mid')
        self.assertEqual(m.filename, 'test.mid')
        self.assertEqual(m.pattern.base_octave, 5)
        self.assertEqual(m.pattern.epoch.day, 1)
        self.assertEqual(m.pattern.epoch.fold, 0)
        self.assertEqual(m.pattern.epoch.hour, 0)
        self.assertEqual(m.pattern.epoch.max.day, 31)
        self.assertEqual(m.pattern.epoch.max.fold, 0)
        self.assertEqual(m.pattern.epoch.max.hour, 23)
        self.assertEqual(m.pattern.epoch.max.microsecond, 999999)
        self.assertEqual(m.pattern.epoch.max.minute, 59)
        self.assertEqual(m.pattern.epoch.max.month, 12)
        self.assertEqual(m.pattern.epoch.max.second, 59)
        self.assertIsNone(m.pattern.epoch.max.tzinfo)
        self.assertEqual(m.pattern.epoch.max.year, 9999)
        self.assertEqual(m.pattern.epoch.microsecond, 0)
        self.assertEqual(m.pattern.epoch.min.day, 1)
        self.assertEqual(m.pattern.epoch.min.fold, 0)
        self.assertEqual(m.pattern.epoch.min.hour, 0)
        self.assertEqual(m.pattern.epoch.min.microsecond, 0)
        self.assertEqual(m.pattern.epoch.min.minute, 0)
        self.assertEqual(m.pattern.epoch.min.month, 1)
        self.assertEqual(m.pattern.epoch.min.second, 0)
        self.assertIsNone(m.pattern.epoch.min.tzinfo)
        self.assertEqual(m.pattern.epoch.min.year, 1)
        self.assertEqual(m.pattern.epoch.minute, 0)
        self.assertEqual(m.pattern.epoch.month, 1)
        self.assertEqual(m.pattern.epoch.resolution.days, 0)
        self.assertEqual(m.pattern.epoch.resolution.microseconds, 1)
        self.assertEqual(m.pattern.epoch.resolution.seconds, 0)
        self.assertEqual(m.pattern.epoch.second, 0)
        self.assertIsNone(m.pattern.epoch.tzinfo)
        self.assertEqual(m.pattern.epoch.year, 1970)
        self.assertEqual(m.pattern.note_chart, [['C'], ['C#', 'Db'], ['D'],
            ['D#', 'Eb'], ['E'], ['F'], ['F#', 'Gb'], ['G'], ['G#', 'Ab'],
            ['A'], ['A#', 'Bb'], ['B']])
        self.assertEqual(m.pattern.octave_range, 1)
        self.assertEqual(m.pattern.outfile, 'test.mid')
        self.assertEqual(m.pattern.seconds_per_year, 5)
        self.assertEqual(m.pattern.tempo, 120)
        self.assertEqual(m.pattern.tracks, [])
        self.assertEqual(m.step_counter, 0)
        m.create(notes)
        self.assertEqual(m.filename, 'test.mid')
        self.assertTrue(m.pattern.MIDIFile.closed)
        self.assertEqual(m.pattern.MIDIFile.header.format, b'\x00\x01')
        self.assertEqual(m.pattern.MIDIFile.header.headerSize,
            b'\x00\x00\x00\x06')
        self.assertEqual(m.pattern.MIDIFile.header.headerString, b'MThd')
        self.assertEqual(m.pattern.MIDIFile.header.numTracks, b'\x00\x01')
        self.assertEqual(m.pattern.MIDIFile.header.ticksPerBeat, b'\x03\xc0')
        self.assertEqual(m.pattern.MIDIFile.numTracks, 1)
        self.assertEqual(m.pattern.base_octave, 5)
        self.assertEqual(m.pattern.epoch.day, 1)
        self.assertEqual(m.pattern.epoch.fold, 0)
        self.assertEqual(m.pattern.epoch.hour, 0)
        self.assertEqual(m.pattern.epoch.max.day, 31)
        self.assertEqual(m.pattern.epoch.max.fold, 0)
        self.assertEqual(m.pattern.epoch.max.hour, 23)
        self.assertEqual(m.pattern.epoch.max.microsecond, 999999)
        self.assertEqual(m.pattern.epoch.max.minute, 59)
        self.assertEqual(m.pattern.epoch.max.month, 12)
        self.assertEqual(m.pattern.epoch.max.second, 59)
        self.assertIsNone(m.pattern.epoch.max.tzinfo)
        self.assertEqual(m.pattern.epoch.max.year, 9999)
        self.assertEqual(m.pattern.epoch.microsecond, 0)
        self.assertEqual(m.pattern.epoch.min.day, 1)
        self.assertEqual(m.pattern.epoch.min.fold, 0)
        self.assertEqual(m.pattern.epoch.min.hour, 0)
        self.assertEqual(m.pattern.epoch.min.microsecond, 0)
        self.assertEqual(m.pattern.epoch.min.minute, 0)
        self.assertEqual(m.pattern.epoch.min.month, 1)
        self.assertEqual(m.pattern.epoch.min.second, 0)
        self.assertIsNone(m.pattern.epoch.min.tzinfo)
        self.assertEqual(m.pattern.epoch.min.year, 1)
        self.assertEqual(m.pattern.epoch.minute, 0)
        self.assertEqual(m.pattern.epoch.month, 1)
        self.assertEqual(m.pattern.epoch.resolution.days, 0)
        self.assertEqual(m.pattern.epoch.resolution.microseconds, 1)
        self.assertEqual(m.pattern.epoch.resolution.seconds, 0)
        self.assertEqual(m.pattern.epoch.second, 0)
        self.assertIsNone(m.pattern.epoch.tzinfo)
        self.assertEqual(m.pattern.epoch.year, 1970)
        self.assertEqual(m.pattern.note_chart, [['C'], ['C#', 'Db'], ['D'],
            ['D#', 'Eb'], ['E'], ['F'], ['F#', 'Gb'], ['G'], ['G#', 'Ab'],
            ['A'], ['A#', 'Bb'], ['B']])
        self.assertEqual(m.pattern.octave_range, 1)
        self.assertEqual(m.pattern.outfile, 'test.mid')
        self.assertEqual(m.pattern.seconds_per_year, 5)
        self.assertEqual(m.pattern.tempo, 120)
        self.assertEqual(m.pattern.tracks, [[[0, 60, 200, 1], [1, 61, 200, 
            1], [2, 62, 200, 1], [3, 63, 200, 1], [4, 64, 200, 1], [5, 65, 
            200, 1], [6, 66, 200, 1], [7, 67, 200, 1], [8, 68, 200, 1], [9,
            69, 200, 1], [10, 70, 200, 1]]])
        self.assertEqual(m.step_counter, 11)
        os.path.exists(os.path.join(os.getcwd(), 'test.mid'))
        os.chdir(os.pardir)
        shutil.rmtree('tmp', ignore_errors=True)
