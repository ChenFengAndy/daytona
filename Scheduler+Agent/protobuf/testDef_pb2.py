# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: testDef.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='testDef.proto',
  package='DaytonaTestDef',
  serialized_pb=_b('\n\rtestDef.proto\x12\x0e\x44\x61ytonaTestDef\"\x90\x03\n\x0fTestInformation\x12:\n\x08testargs\x18\x0b \x03(\x0b\x32(.DaytonaTestDef.TestInformation.TestArgs\x1a\xd5\x01\n\rTestInputData\x12\x0e\n\x06testid\x18\x01 \x02(\x05\x12\x13\n\x0b\x66rameworkid\x18\x02 \x01(\x05\x12\x12\n\nstart_time\x18\x03 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\t\x12\x12\n\nend_status\x18\x05 \x01(\t\x12\x12\n\nend_detail\x18\x06 \x01(\t\x12\x14\n\x0c\x65xechostname\x18\x07 \x01(\t\x12\x14\n\x0cstathostname\x18\x08 \x01(\t\x12\x0f\n\x07timeout\x18\t \x01(\x05\x12\x14\n\x0clocalLogFile\x18\n \x01(\t\x1a\"\n\x08TestArgs\x12\x16\n\x0e\x65xecScriptArgs\x18\x01 \x02(\t\x1a\x45\n\rFrameworkArgs\x12!\n\x19\x65xecution_script_location\x18\x01 \x02(\t\x12\x11\n\tfile_root\x18\x02 \x02(\t\";\n\x07TestDef\x12\x30\n\x07testDef\x18\x01 \x02(\x0b\x32\x1f.DaytonaTestDef.TestInformation')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TESTINFORMATION_TESTINPUTDATA = _descriptor.Descriptor(
  name='TestInputData',
  full_name='DaytonaTestDef.TestInformation.TestInputData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='testid', full_name='DaytonaTestDef.TestInformation.TestInputData.testid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frameworkid', full_name='DaytonaTestDef.TestInformation.TestInputData.frameworkid', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='DaytonaTestDef.TestInformation.TestInputData.start_time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='DaytonaTestDef.TestInformation.TestInputData.end_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_status', full_name='DaytonaTestDef.TestInformation.TestInputData.end_status', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_detail', full_name='DaytonaTestDef.TestInformation.TestInputData.end_detail', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exechostname', full_name='DaytonaTestDef.TestInformation.TestInputData.exechostname', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stathostname', full_name='DaytonaTestDef.TestInformation.TestInputData.stathostname', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='DaytonaTestDef.TestInformation.TestInputData.timeout', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='localLogFile', full_name='DaytonaTestDef.TestInformation.TestInputData.localLogFile', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=327,
)

_TESTINFORMATION_TESTARGS = _descriptor.Descriptor(
  name='TestArgs',
  full_name='DaytonaTestDef.TestInformation.TestArgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='execScriptArgs', full_name='DaytonaTestDef.TestInformation.TestArgs.execScriptArgs', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=329,
  serialized_end=363,
)

_TESTINFORMATION_FRAMEWORKARGS = _descriptor.Descriptor(
  name='FrameworkArgs',
  full_name='DaytonaTestDef.TestInformation.FrameworkArgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='execution_script_location', full_name='DaytonaTestDef.TestInformation.FrameworkArgs.execution_script_location', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_root', full_name='DaytonaTestDef.TestInformation.FrameworkArgs.file_root', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=434,
)

_TESTINFORMATION = _descriptor.Descriptor(
  name='TestInformation',
  full_name='DaytonaTestDef.TestInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='testargs', full_name='DaytonaTestDef.TestInformation.testargs', index=0,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TESTINFORMATION_TESTINPUTDATA, _TESTINFORMATION_TESTARGS, _TESTINFORMATION_FRAMEWORKARGS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=434,
)


_TESTDEF = _descriptor.Descriptor(
  name='TestDef',
  full_name='DaytonaTestDef.TestDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='testDef', full_name='DaytonaTestDef.TestDef.testDef', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=495,
)

_TESTINFORMATION_TESTINPUTDATA.containing_type = _TESTINFORMATION
_TESTINFORMATION_TESTARGS.containing_type = _TESTINFORMATION
_TESTINFORMATION_FRAMEWORKARGS.containing_type = _TESTINFORMATION
_TESTINFORMATION.fields_by_name['testargs'].message_type = _TESTINFORMATION_TESTARGS
_TESTDEF.fields_by_name['testDef'].message_type = _TESTINFORMATION
DESCRIPTOR.message_types_by_name['TestInformation'] = _TESTINFORMATION
DESCRIPTOR.message_types_by_name['TestDef'] = _TESTDEF

TestInformation = _reflection.GeneratedProtocolMessageType('TestInformation', (_message.Message,), dict(

  TestInputData = _reflection.GeneratedProtocolMessageType('TestInputData', (_message.Message,), dict(
    DESCRIPTOR = _TESTINFORMATION_TESTINPUTDATA,
    __module__ = 'testDef_pb2'
    # @@protoc_insertion_point(class_scope:DaytonaTestDef.TestInformation.TestInputData)
    ))
  ,

  TestArgs = _reflection.GeneratedProtocolMessageType('TestArgs', (_message.Message,), dict(
    DESCRIPTOR = _TESTINFORMATION_TESTARGS,
    __module__ = 'testDef_pb2'
    # @@protoc_insertion_point(class_scope:DaytonaTestDef.TestInformation.TestArgs)
    ))
  ,

  FrameworkArgs = _reflection.GeneratedProtocolMessageType('FrameworkArgs', (_message.Message,), dict(
    DESCRIPTOR = _TESTINFORMATION_FRAMEWORKARGS,
    __module__ = 'testDef_pb2'
    # @@protoc_insertion_point(class_scope:DaytonaTestDef.TestInformation.FrameworkArgs)
    ))
  ,
  DESCRIPTOR = _TESTINFORMATION,
  __module__ = 'testDef_pb2'
  # @@protoc_insertion_point(class_scope:DaytonaTestDef.TestInformation)
  ))
_sym_db.RegisterMessage(TestInformation)
_sym_db.RegisterMessage(TestInformation.TestInputData)
_sym_db.RegisterMessage(TestInformation.TestArgs)
_sym_db.RegisterMessage(TestInformation.FrameworkArgs)

TestDef = _reflection.GeneratedProtocolMessageType('TestDef', (_message.Message,), dict(
  DESCRIPTOR = _TESTDEF,
  __module__ = 'testDef_pb2'
  # @@protoc_insertion_point(class_scope:DaytonaTestDef.TestDef)
  ))
_sym_db.RegisterMessage(TestDef)


# @@protoc_insertion_point(module_scope)
