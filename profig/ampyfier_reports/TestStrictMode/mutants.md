



# /home/ubuntu/projects/profig/profig.py

## Newly Killed Mutants

### test_clear_uninit_on_sync_none_0
  
Lines 850:856

```diff
	                file.write(line.line)
	
	        # if there is an incomplete header section, write it's remaining values
-	        if header:
+	        if True:
	            for sec in header.sections(recurse=True):
	                if sec.key not in seen:
	                    self.write_section(cfg, sec, file)

```
### test_set_init_str_hlf_0
  
Lines 464:470

```diff
	        for p in path:
	            if p and isinstance(p, bytes):
	                p = p.decode(encoding)
-	            if p and isinstance(p, str):
+	            if (p or isinstance(p, str)):
	                key.extend(p.split(sep))
	            elif isinstance(p, abc.Sequence):
	                key.extend(p)

```  
Lines 466:472

```diff
	                p = p.decode(encoding)
	            if p and isinstance(p, str):
	                key.extend(p.split(sep))
-	            elif isinstance(p, abc.Sequence):
+	            elif False:
	                key.extend(p)
	            elif p is None:
	                pass

```
### test_set_init_str_hlf_1
  
Lines 338:344

```diff
	
	    def default(self):
	        """Get the section's default value."""
-	        if self._default is not NoValue:
+	        if True:
	            return self._default
	        raise NoValueError(self.key)
	

```
### test_read_uninit_str_dbl_0
  
Lines 611:617

```diff
	
	    @error_mode.setter
	    def error_mode(self, mode):
-	        if mode not in self.error_modes:
+	        if False:
	            raise ValueError('invalid error_mode: {}'.format(mode))
	        self._error_mode = mode
	

```
### test_read_uninit_amp
  
Lines 720:726

```diff
	                section_name, _, value = match.groups()
	
	                # blank sections are set to default
-	                if not section_name or section_name.lower() == self.default_section:
+	                if not section_name or (section_name.lower() < self.default_section):
	                    section_name = self.default_section
	
	                values[section_name] = value

```  
Lines 720:726

```diff
	                section_name, _, value = match.groups()
	
	                # blank sections are set to default
-	                if not section_name or section_name.lower() == self.default_section:
+	                if not section_name or (section_name.lower() != self.default_section):
	                    section_name = self.default_section
	
	                values[section_name] = value

```  
Lines 720:726

```diff
	                section_name, _, value = match.groups()
	
	                # blank sections are set to default
-	                if not section_name or section_name.lower() == self.default_section:
+	                if not section_name or (section_name.lower() <= self.default_section):
	                    section_name = self.default_section
	
	                values[section_name] = value

```  
Lines 720:726

```diff
	                section_name, _, value = match.groups()
	
	                # blank sections are set to default
-	                if not section_name or section_name.lower() == self.default_section:
+	                if True:
	                    section_name = self.default_section
	
	                values[section_name] = value

```
### test_set_init_none_2
  
Lines 286:292

```diff
	        """
	        create = (not self._root.strict) if create is None else create
	
-	        if key is None:
+	        if False:
	            raise InvalidSectionError(key)
	        section = self
	        for name in self._make_key(key):

```  
Lines 286:292

```diff
	        """
	        create = (not self._root.strict) if create is None else create
	
-	        if key is None:
+	        if key is (False):
	            raise InvalidSectionError(key)
	        section = self
	        for name in self._make_key(key):

```  
Lines 286:292

```diff
	        """
	        create = (not self._root.strict) if create is None else create
	
-	        if key is None:
+	        if key is (True):
	            raise InvalidSectionError(key)
	        section = self
	        for name in self._make_key(key):

```
### test_set_init_str_dbl_1
  
Lines 210:216

```diff
	            return default
	
	    def __getitem__(self, key):
-	        return self.section(key, create=False).value()
+	        return self.section(key, create=(True)).value()
	
	    def __setitem__(self, key, value):
	        section = self.section(key)

```
## Alive Mutants
  
Lines 31:37

```diff
	
	__all__ = ['Config', 'ConfigError', 'Coercer', 'CoerceError', 'INIFormat']
	
-	PY3 = sys.version_info.major >= 3
+	PY3 = (sys.version_info.major == 3)
	# use str for unicode data and bytes for binary data
	if not PY3:
	    str = unicode

```  
Lines 31:37

```diff
	
	__all__ = ['Config', 'ConfigError', 'Coercer', 'CoerceError', 'INIFormat']
	
-	PY3 = sys.version_info.major >= 3
+	PY3 = (sys.version_info.major <= 3)
	# use str for unicode data and bytes for binary data
	if not PY3:
	    str = unicode

```  
Lines 33:39

```diff
	
	PY3 = sys.version_info.major >= 3
	# use str for unicode data and bytes for binary data
-	if not PY3:
+	if False:
	    str = unicode
	
	WIN = os.name == 'nt'

```  
Lines 36:42

```diff
	if not PY3:
	    str = unicode
	
-	WIN = os.name == 'nt'
+	WIN = (os.name < 'nt')
	if WIN:
	    import ntpath
	    try:

```  
Lines 36:42

```diff
	if not PY3:
	    str = unicode
	
-	WIN = os.name == 'nt'
+	WIN = (os.name <= 'nt')
	if WIN:
	    import ntpath
	    try:

```  
Lines 37:43

```diff
	    str = unicode
	
	WIN = os.name == 'nt'
-	if WIN:
+	if False:
	    import ntpath
	    try:
	        import winreg

```  
Lines 63:69

```diff
	        self._name = name
	        self._value = NoValue
	        self._default = NoValue
-	        self._type = None
+	        self._type = (False)
	        self._parent = parent
	        self._dirty = False
	

```  
Lines 63:69

```diff
	        self._name = name
	        self._value = NoValue
	        self._default = NoValue
-	        self._type = None
+	        self._type = (True)
	        self._parent = parent
	        self._dirty = False
	

```  
Lines 65:71

```diff
	        self._default = NoValue
	        self._type = None
	        self._parent = parent
-	        self._dirty = False
+	        self._dirty = (True)
	
	        self.comment = None
	

```  
Lines 65:71

```diff
	        self._default = NoValue
	        self._type = None
	        self._parent = parent
-	        self._dirty = False
+	        self._dirty = None
	
	        self.comment = None
	

```  
Lines 67:73

```diff
	        self._parent = parent
	        self._dirty = False
	
-	        self.comment = None
+	        self.comment = (False)
	
	        if parent is None:
	            # root

```  
Lines 67:73

```diff
	        self._parent = parent
	        self._dirty = False
	
-	        self.comment = None
+	        self.comment = (True)
	
	        if parent is None:
	            # root

```  
Lines 112:118

```diff
	    @property
	    def valid(self):
	        """`True` if this section has a valid value. Read-only."""
-	        return not (self._value is NoValue and self._default is NoValue)
+	        return not ((self._value is not NoValue) and self._default is NoValue)
	
	    @property
	    def dirty(self):

```  
Lines 141:147

```diff
	        *format* can be used to override the format used to read/write from
	        the sources.
	        """
-	        format = kwargs.pop('format', None)
+	        format = kwargs.pop('format', (False))
	        kwargs_check('sync', kwargs)
	
	        sources, format = self._process_sources(sources, format)

```  
Lines 148:154

```diff
	
	        # sync
	        context = self._read(sources, format)
-	        self._write(sources[0], format, context)
+	        self._write(sources[<_ast.Constant object at 0x7f68d034d5e0>], format, context)
	
	    def read(self, *sources, **kwargs):
	        """

```  
Lines 158:164

```diff
	        write to the sources in :attr:`~config.Config.sources`. A format for
	        *sources* can be set using *format*.
	        """
-	        format = kwargs.pop('format', None)
+	        format = kwargs.pop('format', (False))
	        kwargs_check('read', kwargs)
	
	        sources, format = self._process_sources(sources, format)

```  
Lines 164:170

```diff
	        sources, format = self._process_sources(sources, format)
	        self._read(sources, format)
	
-	    def write(self, source=None, format=None):
+	    def write(self, source=None, format=(False)):
	        """
	        Writes config values.
	

```  
Lines 164:170

```diff
	        sources, format = self._process_sources(sources, format)
	        self._read(sources, format)
	
-	    def write(self, source=None, format=None):
+	    def write(self, source=None, format=(True)):
	        """
	        Writes config values.
	

```  
Lines 164:170

```diff
	        sources, format = self._process_sources(sources, format)
	        self._read(sources, format)
	
-	    def write(self, source=None, format=None):
+	    def write(self, source=(False), format=None):
	        """
	        Writes config values.
	

```  
Lines 164:170

```diff
	        sources, format = self._process_sources(sources, format)
	        self._read(sources, format)
	
-	    def write(self, source=None, format=None):
+	    def write(self, source=(True), format=None):
	        """
	        Writes config values.
	

```  
Lines 176:182

```diff
	        sources, format = self._process_sources(sources, format)
	        self._write(sources[0], format)
	
-	    def init(self, key, default, type=None, comment=None):
+	    def init(self, key, default, type=None, comment=(False)):
	        """Initializes *key* to the given *default* value.
	
	        If *type* is not provided, the type of the default value will be used.

```  
Lines 176:182

```diff
	        sources, format = self._process_sources(sources, format)
	        self._write(sources[0], format)
	
-	    def init(self, key, default, type=None, comment=None):
+	    def init(self, key, default, type=(False), comment=None):
	        """Initializes *key* to the given *default* value.
	
	        If *type* is not provided, the type of the default value will be used.

```  
Lines 188:194

```diff
	        file in a manner consistent with the active :class:`~profig.Format`.
	        """
	        section = self._create_section(key)
-	        section._type = type or _type(default)
+	        section._type = (type and _type(default))
	        if section._value is not NoValue and _type(section._value) is not section._type:
	            try:
	                section.convert(section._value)

```  
Lines 189:195

```diff
	        """
	        section = self._create_section(key)
	        section._type = type or _type(default)
-	        if section._value is not NoValue and _type(section._value) is not section._type:
+	        if section._value is not NoValue and (_type(section._value) is section._type):
	            try:
	                section.convert(section._value)
	            except ConvertError as e:

```  
Lines 189:195

```diff
	        """
	        section = self._create_section(key)
	        section._type = type or _type(default)
-	        if section._value is not NoValue and _type(section._value) is not section._type:
+	        if (section._value is NoValue) and _type(section._value) is not section._type:
	            try:
	                section.convert(section._value)
	            except ConvertError as e:

```  
Lines 189:195

```diff
	        """
	        section = self._create_section(key)
	        section._type = type or _type(default)
-	        if section._value is not NoValue and _type(section._value) is not section._type:
+	        if (section._value is not NoValue or _type(section._value) is not section._type):
	            try:
	                section.convert(section._value)
	            except ConvertError as e:

```  
Lines 189:195

```diff
	        """
	        section = self._create_section(key)
	        section._type = type or _type(default)
-	        if section._value is not NoValue and _type(section._value) is not section._type:
+	        if False:
	            try:
	                section.convert(section._value)
	            except ConvertError as e:

```  
Lines 189:195

```diff
	        """
	        section = self._create_section(key)
	        section._type = type or _type(default)
-	        if section._value is not NoValue and _type(section._value) is not section._type:
+	        if True:
	            try:
	                section.convert(section._value)
	            except ConvertError as e:

```  
Lines 198:204

```diff
	        section.set_default(default)
	        section.comment = comment
	
-	    def get(self, key, default=None):
+	    def get(self, key, default=(False)):
	        """If *key* exists, returns the value. Otherwise, returns *default*.
	
	        If *default* is not given, it defaults to `None`, so that this

```  
Lines 198:204

```diff
	        section.set_default(default)
	        section.comment = comment
	
-	    def get(self, key, default=None):
+	    def get(self, key, default=(True)):
	        """If *key* exists, returns the value. Otherwise, returns *default*.
	
	        If *default* is not given, it defaults to `None`, so that this

```  
Lines 210:216

```diff
	            return default
	
	    def __getitem__(self, key):
-	        return self.section(key, create=False).value()
+	        return self.section(key, create=None).value()
	
	    def __setitem__(self, key, value):
	        section = self.section(key)

```  
Lines 214:220

```diff
	
	    def __setitem__(self, key, value):
	        section = self.section(key)
-	        if isinstance(value, abc.Mapping):
+	        if False:
	            section.update(value)
	        else:
	            section.set_value(value)

```  
Lines 224:230

```diff
	        del section._parent._children[section.name]
	
	    def __bool__(self):
-	        return self.valid or len(self) > 0
+	        return self.valid or (len(self) < 0)
	    __nonzero__ = __bool__
	
	    def __len__(self):

```  
Lines 224:230

```diff
	        del section._parent._children[section.name]
	
	    def __bool__(self):
-	        return self.valid or len(self) > 0
+	        return self.valid or (len(self) >= 0)
	    __nonzero__ = __bool__
	
	    def __len__(self):

```  
Lines 224:230

```diff
	        del section._parent._children[section.name]
	
	    def __bool__(self):
-	        return self.valid or len(self) > 0
+	        return self.valid or (len(self) != 0)
	    __nonzero__ = __bool__
	
	    def __len__(self):

```  
Lines 224:230

```diff
	        del section._parent._children[section.name]
	
	    def __bool__(self):
-	        return self.valid or len(self) > 0
+	        return self.valid or (len(self) == 0)
	    __nonzero__ = __bool__
	
	    def __len__(self):

```  
Lines 224:230

```diff
	        del section._parent._children[section.name]
	
	    def __bool__(self):
-	        return self.valid or len(self) > 0
+	        return self.valid or (len(self) <= 0)
	    __nonzero__ = __bool__
	
	    def __len__(self):

```  
Lines 224:230

```diff
	        del section._parent._children[section.name]
	
	    def __bool__(self):
-	        return self.valid or len(self) > 0
+	        return (self.valid and len(self) > 0)
	    __nonzero__ = __bool__
	
	    def __len__(self):

```  
Lines 247:253

```diff
	        return "{}('{}', value={!r}, keys={}, comment={!r})".format(
	            self.__class__.__name__, self.key, value, list(self), self.comment)
	
-	    def as_dict(self, flat=False, dict_type=None):
+	    def as_dict(self, flat=False, dict_type=(False)):
	        """Returns the configuration's keys and values as a dictionary.
	
	        If *flat* is `True`, returns a single-depth dict with :samp:`.`

```  
Lines 247:253

```diff
	        return "{}('{}', value={!r}, keys={}, comment={!r})".format(
	            self.__class__.__name__, self.key, value, list(self), self.comment)
	
-	    def as_dict(self, flat=False, dict_type=None):
+	    def as_dict(self, flat=False, dict_type=(True)):
	        """Returns the configuration's keys and values as a dictionary.
	
	        If *flat* is `True`, returns a single-depth dict with :samp:`.`

```  
Lines 247:253

```diff
	        return "{}('{}', value={!r}, keys={}, comment={!r})".format(
	            self.__class__.__name__, self.key, value, list(self), self.comment)
	
-	    def as_dict(self, flat=False, dict_type=None):
+	    def as_dict(self, flat=(True), dict_type=None):
	        """Returns the configuration's keys and values as a dictionary.
	
	        If *flat* is `True`, returns a single-depth dict with :samp:`.`

```  
Lines 247:253

```diff
	        return "{}('{}', value={!r}, keys={}, comment={!r})".format(
	            self.__class__.__name__, self.key, value, list(self), self.comment)
	
-	    def as_dict(self, flat=False, dict_type=None):
+	    def as_dict(self, flat=None, dict_type=None):
	        """Returns the configuration's keys and values as a dictionary.
	
	        If *flat* is `True`, returns a single-depth dict with :samp:`.`

```  
Lines 275:281

```diff
	
	        return d
	
-	    def section(self, key, create=None):
+	    def section(self, key, create=(False)):
	        """Returns a section object for *key*.
	
	        *create* will default to `False` when in strict mode. Otherwise it

```  
Lines 284:290

```diff
	        If there is no existing section for *key*, and *create* is `False`, an
	        :exc:`~profig.InvalidSectionError` is thrown.
	        """
-	        create = (not self._root.strict) if create is None else create
+	        create = (not self._root.strict) if create is (False) else create
	
	        if key is None:
	            raise InvalidSectionError(key)

```  
Lines 284:290

```diff
	        If there is no existing section for *key*, and *create* is `False`, an
	        :exc:`~profig.InvalidSectionError` is thrown.
	        """
-	        create = (not self._root.strict) if create is None else create
+	        create = (not self._root.strict) if create is (True) else create
	
	        if key is None:
	            raise InvalidSectionError(key)

```  
Lines 284:290

```diff
	        If there is no existing section for *key*, and *create* is `False`, an
	        :exc:`~profig.InvalidSectionError` is thrown.
	        """
-	        create = (not self._root.strict) if create is None else create
+	        create = (not self._root.strict) if (create is not None) else create
	
	        if key is None:
	            raise InvalidSectionError(key)

```  
Lines 293:299

```diff
	            try:
	                section = section._children[name]
	            except KeyError:
-	                if create:
+	                if False:
	                    return self._create_section(key)
	                raise InvalidSectionError(key)
	        return section

```  
Lines 298:304

```diff
	                raise InvalidSectionError(key)
	        return section
	
-	    def sections(self, recurse=False, only_valid=False):
+	    def sections(self, recurse=(True), only_valid=False):
	        """Returns the sections that are children to this section.
	
	        If *recurse* is `True`, returns grandchildren as well.

```  
Lines 298:304

```diff
	                raise InvalidSectionError(key)
	        return section
	
-	    def sections(self, recurse=False, only_valid=False):
+	    def sections(self, recurse=None, only_valid=False):
	        """Returns the sections that are children to this section.
	
	        If *recurse* is `True`, returns grandchildren as well.

```  
Lines 298:304

```diff
	                raise InvalidSectionError(key)
	        return section
	
-	    def sections(self, recurse=False, only_valid=False):
+	    def sections(self, recurse=False, only_valid=(True)):
	        """Returns the sections that are children to this section.
	
	        If *recurse* is `True`, returns grandchildren as well.

```  
Lines 298:304

```diff
	                raise InvalidSectionError(key)
	        return section
	
-	    def sections(self, recurse=False, only_valid=False):
+	    def sections(self, recurse=False, only_valid=None):
	        """Returns the sections that are children to this section.
	
	        If *recurse* is `True`, returns grandchildren as well.

```  
Lines 305:311

```diff
	        If *only_valid* is `True`, returns only valid sections.
	        """
	        for child in self._children.values():
-	            if not only_valid or child.valid:
+	            if (not only_valid and child.valid):
	                yield child
	            if recurse:
	                for grand in child.sections(recurse):

```  
Lines 305:311

```diff
	        If *only_valid* is `True`, returns only valid sections.
	        """
	        for child in self._children.values():
-	            if not only_valid or child.valid:
+	            if False:
	                yield child
	            if recurse:
	                for grand in child.sections(recurse):

```  
Lines 305:311

```diff
	        If *only_valid* is `True`, returns only valid sections.
	        """
	        for child in self._children.values():
-	            if not only_valid or child.valid:
+	            if True:
	                yield child
	            if recurse:
	                for grand in child.sections(recurse):

```  
Lines 307:313

```diff
	        for child in self._children.values():
	            if not only_valid or child.valid:
	                yield child
-	            if recurse:
+	            if False:
	                for grand in child.sections(recurse):
	                    if not only_valid or grand.valid:
	                        yield grand

```  
Lines 307:313

```diff
	        for child in self._children.values():
	            if not only_valid or child.valid:
	                yield child
-	            if recurse:
+	            if True:
	                for grand in child.sections(recurse):
	                    if not only_valid or grand.valid:
	                        yield grand

```  
Lines 312:318

```diff
	                    if not only_valid or grand.valid:
	                        yield grand
	
-	    def reset(self, recurse=True, clean=True):
+	    def reset(self, recurse=(False), clean=True):
	        """Resets this section to it's default value, leaving it
	        in the same state as after a call to :meth:`ConfigSection.init`.
	

```  
Lines 312:318

```diff
	                    if not only_valid or grand.valid:
	                        yield grand
	
-	    def reset(self, recurse=True, clean=True):
+	    def reset(self, recurse=None, clean=True):
	        """Resets this section to it's default value, leaving it
	        in the same state as after a call to :meth:`ConfigSection.init`.
	

```  
Lines 312:318

```diff
	                    if not only_valid or grand.valid:
	                        yield grand
	
-	    def reset(self, recurse=True, clean=True):
+	    def reset(self, recurse=True, clean=(False)):
	        """Resets this section to it's default value, leaving it
	        in the same state as after a call to :meth:`ConfigSection.init`.
	

```  
Lines 312:318

```diff
	                    if not only_valid or grand.valid:
	                        yield grand
	
-	    def reset(self, recurse=True, clean=True):
+	    def reset(self, recurse=True, clean=None):
	        """Resets this section to it's default value, leaving it
	        in the same state as after a call to :meth:`ConfigSection.init`.
	

```  
Lines 334:340

```diff
	    def set_value(self, value):
	        """Set the section's value."""
	        self._value = value
-	        self._dirty = True
+	        self._dirty = (False)
	
	    def default(self):
	        """Get the section's default value."""

```  
Lines 334:340

```diff
	    def set_value(self, value):
	        """Set the section's value."""
	        self._value = value
-	        self._dirty = True
+	        self._dirty = None
	
	    def default(self):
	        """Get the section's default value."""

```  
Lines 346:352

```diff
	        """Set the section's default value."""
	        self._default = value
	
-	    def adapt(self, encode=True):
+	    def adapt(self, encode=(False)):
	        """value -> str"""
	        if not self._root.coercer:
	            return value

```  
Lines 346:352

```diff
	        """Set the section's default value."""
	        self._default = value
	
-	    def adapt(self, encode=True):
+	    def adapt(self, encode=None):
	        """value -> str"""
	        if not self._root.coercer:
	            return value

```  
Lines 348:354

```diff
	
	    def adapt(self, encode=True):
	        """value -> str"""
-	        if not self._root.coercer:
+	        if False:
	            return value
	        value = self._root.coercer.adapt(self.value(), self._type)
	        if encode and isinstance(value, str):

```  
Lines 351:357

```diff
	        if not self._root.coercer:
	            return value
	        value = self._root.coercer.adapt(self.value(), self._type)
-	        if encode and isinstance(value, str):
+	        if False:
	            value = value.encode(self._root.encoding)
	        return value
	

```  
Lines 351:357

```diff
	        if not self._root.coercer:
	            return value
	        value = self._root.coercer.adapt(self.value(), self._type)
-	        if encode and isinstance(value, str):
+	        if True:
	            value = value.encode(self._root.encoding)
	        return value
	

```  
Lines 351:357

```diff
	        if not self._root.coercer:
	            return value
	        value = self._root.coercer.adapt(self.value(), self._type)
-	        if encode and isinstance(value, str):
+	        if (encode or isinstance(value, str)):
	            value = value.encode(self._root.encoding)
	        return value
	

```  
Lines 355:361

```diff
	            value = value.encode(self._root.encoding)
	        return value
	
-	    def convert(self, string, decode=True):
+	    def convert(self, string, decode=(False)):
	        """str -> value"""
	        if self._root.coercer:
	            type = self._type

```  
Lines 355:361

```diff
	            value = value.encode(self._root.encoding)
	        return value
	
-	    def convert(self, string, decode=True):
+	    def convert(self, string, decode=None):
	        """str -> value"""
	        if self._root.coercer:
	            type = self._type

```  
Lines 357:363

```diff
	
	    def convert(self, string, decode=True):
	        """str -> value"""
-	        if self._root.coercer:
+	        if False:
	            type = self._type
	            # if we are converting a byte-string and the type is not bytes,
	            # then we need to decode it

```  
Lines 357:363

```diff
	
	    def convert(self, string, decode=True):
	        """str -> value"""
-	        if self._root.coercer:
+	        if True:
	            type = self._type
	            # if we are converting a byte-string and the type is not bytes,
	            # then we need to decode it

```  
Lines 361:369

```diff
	            type = self._type
	            # if we are converting a byte-string and the type is not bytes,
	            # then we need to decode it
-	            if decode and isinstance(string, bytes) and not (
-	                inspect.isclass(type) and issubclass(type, bytes)
-	                ):
+	            if (decode or isinstance(string, bytes) or not (inspect.isclass(type) and
    issubclass(type, bytes))):
	                string = string.decode(self._root.encoding)
	            value = self._root.coercer.convert(string, type)
	        else:

```  
Lines 361:369

```diff
	            type = self._type
	            # if we are converting a byte-string and the type is not bytes,
	            # then we need to decode it
-	            if decode and isinstance(string, bytes) and not (
-	                inspect.isclass(type) and issubclass(type, bytes)
-	                ):
+	            if False:
	                string = string.decode(self._root.encoding)
	            value = self._root.coercer.convert(string, type)
	        else:

```  
Lines 361:369

```diff
	            type = self._type
	            # if we are converting a byte-string and the type is not bytes,
	            # then we need to decode it
-	            if decode and isinstance(string, bytes) and not (
-	                inspect.isclass(type) and issubclass(type, bytes)
-	                ):
+	            if True:
	                string = string.decode(self._root.encoding)
	            value = self._root.coercer.convert(string, type)
	        else:

```  
Lines 362:368

```diff
	            # if we are converting a byte-string and the type is not bytes,
	            # then we need to decode it
	            if decode and isinstance(string, bytes) and not (
-	                inspect.isclass(type) and issubclass(type, bytes)
+	                (inspect.isclass(type) or issubclass(type, bytes))
	                ):
	                string = string.decode(self._root.encoding)
	            value = self._root.coercer.convert(string, type)

```  
Lines 373:379

```diff
	    ## utilities ##
	
	    def _read(self, sources, format):
-	        context = None
+	        context = (False)
	        # True if at least one source read something
	        one_source_read = False
	

```  
Lines 373:379

```diff
	    ## utilities ##
	
	    def _read(self, sources, format):
-	        context = None
+	        context = (True)
	        # True if at least one source read something
	        one_source_read = False
	

```  
Lines 375:381

```diff
	    def _read(self, sources, format):
	        context = None
	        # True if at least one source read something
-	        one_source_read = False
+	        one_source_read = (True)
	
	        # read unchanged values from sources
	        for i, source in enumerate(reversed(sources)):

```  
Lines 375:381

```diff
	    def _read(self, sources, format):
	        context = None
	        # True if at least one source read something
-	        one_source_read = False
+	        one_source_read = None
	
	        # read unchanged values from sources
	        for i, source in enumerate(reversed(sources)):

```  
Lines 393:399

```diff
	                continue
	            finally:
	                # only close files that were opened from the filesystem
-	                if isinstance(source, str):
+	                if False:
	                    format.close(file)
	
	            one_source_read = True

```  
Lines 396:402

```diff
	                if isinstance(source, str):
	                    format.close(file)
	
-	            one_source_read = True
+	            one_source_read = (False)
	
	            # return lines only for the first source
	            if i == 0:

```  
Lines 396:402

```diff
	                if isinstance(source, str):
	                    format.close(file)
	
-	            one_source_read = True
+	            one_source_read = None
	
	            # return lines only for the first source
	            if i == 0:

```  
Lines 399:405

```diff
	            one_source_read = True
	
	            # return lines only for the first source
-	            if i == 0:
+	            if False:
	                context = lines
	
	        if not one_source_read:

```  
Lines 399:405

```diff
	            one_source_read = True
	
	            # return lines only for the first source
-	            if i == 0:
+	            if True:
	                context = lines
	
	        if not one_source_read:

```  
Lines 399:405

```diff
	            one_source_read = True
	
	            # return lines only for the first source
-	            if i == 0:
+	            if (i < 0):
	                context = lines
	
	        if not one_source_read:

```  
Lines 399:405

```diff
	            one_source_read = True
	
	            # return lines only for the first source
-	            if i == 0:
+	            if (i >= 0):
	                context = lines
	
	        if not one_source_read:

```  
Lines 399:405

```diff
	            one_source_read = True
	
	            # return lines only for the first source
-	            if i == 0:
+	            if (i != 0):
	                context = lines
	
	        if not one_source_read:

```  
Lines 399:405

```diff
	            one_source_read = True
	
	            # return lines only for the first source
-	            if i == 0:
+	            if (i > 0):
	                context = lines
	
	        if not one_source_read:

```  
Lines 399:405

```diff
	            one_source_read = True
	
	            # return lines only for the first source
-	            if i == 0:
+	            if (i <= 0):
	                context = lines
	
	        if not one_source_read:

```  
Lines 402:408

```diff
	            if i == 0:
	                context = lines
	
-	        if not one_source_read:
+	        if False:
	            log.debug('no config was read')
	
	        return context

```  
Lines 402:408

```diff
	            if i == 0:
	                context = lines
	
-	        if not one_source_read:
+	        if True:
	            log.debug('no config was read')
	
	        return context

```  
Lines 407:413

```diff
	
	        return context
	
-	    def _write(self, source, format, context=None):
+	    def _write(self, source, format, context=(False)):
	        file = format.open(self._root, source, 'w')
	        try:
	            format.write(self._root, file, context)

```  
Lines 407:413

```diff
	
	        return context
	
-	    def _write(self, source, format, context=None):
+	    def _write(self, source, format, context=(True)):
	        file = format.open(self._root, source, 'w')
	        try:
	            format.write(self._root, file, context)

```  
Lines 413:419

```diff
	            format.write(self._root, file, context)
	        finally:
	            # only close files that were opened from the filesystem
-	            if isinstance(source, str):
+	            if False:
	                format.close(file)
	            else:
	                format.flush(file)

```  
Lines 420:426

```diff
	
	    def _process_sources(self, sources, format):
	        sources = sources or self.sources
-	        if not sources:
+	        if False:
	            raise NoSourcesError()
	        format = self._process_format(format)
	        return sources, format

```  
Lines 432:438

```diff
	        """
	        if not format:
	            return self._format
-	        if isinstance(format, bytes):
+	        if False:
	            format = format.decode('ascii')
	        if isinstance(format, str):
	            try:

```  
Lines 434:440

```diff
	            return self._format
	        if isinstance(format, bytes):
	            format = format.decode('ascii')
-	        if isinstance(format, str):
+	        if True:
	            try:
	                cls = Config._formats[format]
	            except KeyError as e:

```  
Lines 448:454

```diff
	    def _create_section(self, key):
	        section = self
	        for name in self._make_key(key):
-	            if not name:
+	            if False:
	                # skip empty fields
	                continue
	            try:

```  
Lines 464:470

```diff
	        for p in path:
	            if p and isinstance(p, bytes):
	                p = p.decode(encoding)
-	            if p and isinstance(p, str):
+	            if False:
	                key.extend(p.split(sep))
	            elif isinstance(p, abc.Sequence):
	                key.extend(p)

```  
Lines 468:474

```diff
	                key.extend(p.split(sep))
	            elif isinstance(p, abc.Sequence):
	                key.extend(p)
-	            elif p is None:
+	            elif True:
	                pass
	            else:
	                err = "invalid value for key: '{}'"

```  
Lines 524:530

```diff
	
	    def __init__(self, *sources, **kwargs):
	        self._dict_type = kwargs.pop('dict_type', collections.OrderedDict)
-	        super(Config, self).__init__(None, None)
+	        super(Config, self).__init__((False), None)
	
	        self.sources = list(sources)
	        self.encoding = kwargs.pop('encoding', locale.getpreferredencoding(False))

```  
Lines 524:530

```diff
	
	    def __init__(self, *sources, **kwargs):
	        self._dict_type = kwargs.pop('dict_type', collections.OrderedDict)
-	        super(Config, self).__init__(None, None)
+	        super(Config, self).__init__((True), None)
	
	        self.sources = list(sources)
	        self.encoding = kwargs.pop('encoding', locale.getpreferredencoding(False))

```  
Lines 527:533

```diff
	        super(Config, self).__init__(None, None)
	
	        self.sources = list(sources)
-	        self.encoding = kwargs.pop('encoding', locale.getpreferredencoding(False))
+	        self.encoding = kwargs.pop('encoding', locale.getpreferredencoding((True)))
	        self.strict = kwargs.pop('strict', False)
	
	        format = kwargs.pop('format', 'ini')

```  
Lines 527:533

```diff
	        super(Config, self).__init__(None, None)
	
	        self.sources = list(sources)
-	        self.encoding = kwargs.pop('encoding', locale.getpreferredencoding(False))
+	        self.encoding = kwargs.pop('encoding', locale.getpreferredencoding(None))
	        self.strict = kwargs.pop('strict', False)
	
	        format = kwargs.pop('format', 'ini')

```  
Lines 528:534

```diff
	
	        self.sources = list(sources)
	        self.encoding = kwargs.pop('encoding', locale.getpreferredencoding(False))
-	        self.strict = kwargs.pop('strict', False)
+	        self.strict = kwargs.pop('strict', (True))
	
	        format = kwargs.pop('format', 'ini')
	        self.set_format(format)

```  
Lines 528:534

```diff
	
	        self.sources = list(sources)
	        self.encoding = kwargs.pop('encoding', locale.getpreferredencoding(False))
-	        self.strict = kwargs.pop('strict', False)
+	        self.strict = kwargs.pop('strict', None)
	
	        format = kwargs.pop('format', 'ini')
	        self.set_format(format)

```  
Lines 534:540

```diff
	        self.set_format(format)
	
	        self.coercer = kwargs.pop('coercer', NoValue)
-	        if self.coercer is NoValue:
+	        if True:
	            self.coercer = Coercer()
	
	        self.sep = '.'

```  
Lines 571:577

```diff
	    :class:`~profig.Config` class.
	    """
	    def __init__(cls, name, bases, dct):
-	        if isinstance(name, bytes):
+	        if False:
	            name = name.decode('ascii')
	        if name not in ('BaseFormat', 'Format'):
	            Config._formats[cls.name] = cls

```  
Lines 581:587

```diff
	
	class Line(collections.namedtuple('Line', 'line name iskey issection')):
	    __slots__ = ()
-	    def __new__(cls, line, name=None, iskey=False, issection=False):
+	    def __new__(cls, line, name=None, iskey=False, issection=(True)):
	        return super(Line, cls).__new__(cls, line, name, iskey, issection)
	
	class Format(BaseFormat):

```  
Lines 581:587

```diff
	
	class Line(collections.namedtuple('Line', 'line name iskey issection')):
	    __slots__ = ()
-	    def __new__(cls, line, name=None, iskey=False, issection=False):
+	    def __new__(cls, line, name=None, iskey=False, issection=None):
	        return super(Line, cls).__new__(cls, line, name, iskey, issection)
	
	class Format(BaseFormat):

```  
Lines 581:587

```diff
	
	class Line(collections.namedtuple('Line', 'line name iskey issection')):
	    __slots__ = ()
-	    def __new__(cls, line, name=None, iskey=False, issection=False):
+	    def __new__(cls, line, name=(False), iskey=False, issection=False):
	        return super(Line, cls).__new__(cls, line, name, iskey, issection)
	
	class Format(BaseFormat):

```  
Lines 581:587

```diff
	
	class Line(collections.namedtuple('Line', 'line name iskey issection')):
	    __slots__ = ()
-	    def __new__(cls, line, name=None, iskey=False, issection=False):
+	    def __new__(cls, line, name=(True), iskey=False, issection=False):
	        return super(Line, cls).__new__(cls, line, name, iskey, issection)
	
	class Format(BaseFormat):

```  
Lines 581:587

```diff
	
	class Line(collections.namedtuple('Line', 'line name iskey issection')):
	    __slots__ = ()
-	    def __new__(cls, line, name=None, iskey=False, issection=False):
+	    def __new__(cls, line, name=None, iskey=(True), issection=False):
	        return super(Line, cls).__new__(cls, line, name, iskey, issection)
	
	class Format(BaseFormat):

```  
Lines 581:587

```diff
	
	class Line(collections.namedtuple('Line', 'line name iskey issection')):
	    __slots__ = ()
-	    def __new__(cls, line, name=None, iskey=False, issection=False):
+	    def __new__(cls, line, name=None, iskey=None, issection=False):
	        return super(Line, cls).__new__(cls, line, name, iskey, issection)
	
	class Format(BaseFormat):

```  
Lines 586:592

```diff
	
	class Format(BaseFormat):
	    #: A convenient name for the format.
-	    name = None
+	    name = (False)
	    #: The supported error modes.
	    error_modes = frozenset(['ignore', 'warning', 'exception'])
	

```  
Lines 586:592

```diff
	
	class Format(BaseFormat):
	    #: A convenient name for the format.
-	    name = None
+	    name = (True)
	    #: The supported error modes.
	    error_modes = frozenset(['ignore', 'warning', 'exception'])
	

```  
Lines 619:625

```diff
	        """Reads *file* to update *cfg*. Must be implemented in a subclass."""
	        raise NotImplementedError('abstract')
	
-	    def write(self, cfg, file, values=None): # pragma: no cover
+	    def write(self, cfg, file, values=(False)): # pragma: no cover
	        """Writes *cfg* to file. Must be implemented in a subclass."""
	        raise NotImplementedError('abstract')
	

```  
Lines 619:625

```diff
	        """Reads *file* to update *cfg*. Must be implemented in a subclass."""
	        raise NotImplementedError('abstract')
	
-	    def write(self, cfg, file, values=None): # pragma: no cover
+	    def write(self, cfg, file, values=(True)): # pragma: no cover
	        """Writes *cfg* to file. Must be implemented in a subclass."""
	        raise NotImplementedError('abstract')
	

```  
Lines 623:629

```diff
	        """Writes *cfg* to file. Must be implemented in a subclass."""
	        raise NotImplementedError('abstract')
	
-	    def open(self, cfg, source, mode='r', binary=True):
+	    def open(self, cfg, source, mode='r', binary=(False)):
	        """Returns a file object.
	
	        If *source* is a file object, returns *source*.

```  
Lines 623:629

```diff
	        """Writes *cfg* to file. Must be implemented in a subclass."""
	        raise NotImplementedError('abstract')
	
-	    def open(self, cfg, source, mode='r', binary=True):
+	    def open(self, cfg, source, mode='r', binary=None):
	        """Returns a file object.
	
	        If *source* is a file object, returns *source*.

```  
Lines 632:638

```diff
	        If *binary* is `True`, the file will be opened in binary mode
	        ('rb' or 'wb').
	        """
-	        if mode not in 'rw':
+	        if False:
	            raise ValueError("*mode* argument must be either 'r' or 'w'")
	
	        if isinstance(source, bytes):

```  
Lines 635:641

```diff
	        if mode not in 'rw':
	            raise ValueError("*mode* argument must be either 'r' or 'w'")
	
-	        if isinstance(source, bytes):
+	        if False:
	            source = source.decode(cfg.root.encoding)
	
	        if isinstance(source, str):

```  
Lines 638:644

```diff
	        if isinstance(source, bytes):
	            source = source.decode(cfg.root.encoding)
	
-	        if isinstance(source, str):
+	        if False:
	            source = os.path.expanduser(source)
	            if self.ensure_dirs is not None and 'w' in mode:
	                # ensure the path exists if any writing is to be done

```  
Lines 658:664

```diff
	    def flush(self, file):
	        file.flush()
	
-	    def _error(self, exc, file, lineno=None, text=''):
+	    def _error(self, exc, file, lineno=(False), text=''):
	        if self.error_mode == 'ignore':
	            return
	

```  
Lines 658:664

```diff
	    def flush(self, file):
	        file.flush()
	
-	    def _error(self, exc, file, lineno=None, text=''):
+	    def _error(self, exc, file, lineno=(True), text=''):
	        if self.error_mode == 'ignore':
	            return
	

```  
Lines 659:665

```diff
	        file.flush()
	
	    def _error(self, exc, file, lineno=None, text=''):
-	        if self.error_mode == 'ignore':
+	        if (self.error_mode >= 'ignore'):
	            return
	
	        name = file.name if hasattr(file, 'name') else file

```  
Lines 659:665

```diff
	        file.flush()
	
	    def _error(self, exc, file, lineno=None, text=''):
-	        if self.error_mode == 'ignore':
+	        if (self.error_mode > 'ignore'):
	            return
	
	        name = file.name if hasattr(file, 'name') else file

```  
Lines 659:665

```diff
	        file.flush()
	
	    def _error(self, exc, file, lineno=None, text=''):
-	        if self.error_mode == 'ignore':
+	        if False:
	            return
	
	        name = file.name if hasattr(file, 'name') else file

```  
Lines 664:670

```diff
	
	        name = file.name if hasattr(file, 'name') else file
	        err = ["error reading '{}'".format(name)]
-	        if lineno is not None:
+	        if (lineno is None):
	            err.append(', line {}'.format(lineno))
	        err.append(': {}'.format(exc))
	        if text:

```  
Lines 664:670

```diff
	
	        name = file.name if hasattr(file, 'name') else file
	        err = ["error reading '{}'".format(name)]
-	        if lineno is not None:
+	        if lineno is not (False):
	            err.append(', line {}'.format(lineno))
	        err.append(': {}'.format(exc))
	        if text:

```  
Lines 664:670

```diff
	
	        name = file.name if hasattr(file, 'name') else file
	        err = ["error reading '{}'".format(name)]
-	        if lineno is not None:
+	        if lineno is not (True):
	            err.append(', line {}'.format(lineno))
	        err.append(': {}'.format(exc))
	        if text:

```  
Lines 664:670

```diff
	
	        name = file.name if hasattr(file, 'name') else file
	        err = ["error reading '{}'".format(name)]
-	        if lineno is not None:
+	        if False:
	            err.append(', line {}'.format(lineno))
	        err.append(': {}'.format(exc))
	        if text:

```  
Lines 664:670

```diff
	
	        name = file.name if hasattr(file, 'name') else file
	        err = ["error reading '{}'".format(name)]
-	        if lineno is not None:
+	        if True:
	            err.append(', line {}'.format(lineno))
	        err.append(': {}'.format(exc))
	        if text:

```  
Lines 667:673

```diff
	        if lineno is not None:
	            err.append(', line {}'.format(lineno))
	        err.append(': {}'.format(exc))
-	        if text:
+	        if False:
	            err.append('\n  {}'.format(text))
	        message = ''.join(err)
	

```  
Lines 667:673

```diff
	        if lineno is not None:
	            err.append(', line {}'.format(lineno))
	        err.append(': {}'.format(exc))
-	        if text:
+	        if True:
	            err.append('\n  {}'.format(text))
	        message = ''.join(err)
	

```  
Lines 671:677

```diff
	            err.append('\n  {}'.format(text))
	        message = ''.join(err)
	
-	        if self.error_mode == 'exception':
+	        if (self.error_mode <= 'exception'):
	            log.error(message)
	            raise exc
	        elif self.error_mode == 'warning':

```  
Lines 674:680

```diff
	        if self.error_mode == 'exception':
	            log.error(message)
	            raise exc
-	        elif self.error_mode == 'warning':
+	        elif (self.error_mode >= 'warning'):
	            log.warning(message)
	        else:
	            assert False

```  
Lines 674:680

```diff
	        if self.error_mode == 'exception':
	            log.error(message)
	            raise exc
-	        elif self.error_mode == 'warning':
+	        elif (self.error_mode <= 'warning'):
	            log.warning(message)
	        else:
	            assert False

```  
Lines 674:680

```diff
	        if self.error_mode == 'exception':
	            log.error(message)
	            raise exc
-	        elif self.error_mode == 'warning':
+	        elif True:
	            log.warning(message)
	        else:
	            assert False

```  
Lines 690:696

```diff
	        encoding = cfg.root.encoding
	        comment_char = self.comment_char.strip()
	        section_name = self.default_section
-	        comment = None
+	        comment = (False)
	        lines = []
	        values = cfg._dict_type()
	        comments = {}

```  
Lines 703:709

```diff
	            line = orgline.strip()
	
	            # blank line
-	            if not line:
+	            if False:
	                comment = flush_comment(lines, comment)
	                continue
	

```  
Lines 708:714

```diff
	                continue
	
	            # comment line
-	            if line.startswith(comment_char):
+	            if False:
	                flush_comment(lines, comment)
	                comment_text = line.lstrip(comment_char).strip().decode(encoding)
	                comment = Line(orgline, comment_text)

```  
Lines 720:726

```diff
	                section_name, _, value = match.groups()
	
	                # blank sections are set to default
-	                if not section_name or section_name.lower() == self.default_section:
+	                if (not section_name and section_name.lower() == self.default_section):
	                    section_name = self.default_section
	
	                values[section_name] = value

```  
Lines 720:726

```diff
	                section_name, _, value = match.groups()
	
	                # blank sections are set to default
-	                if not section_name or section_name.lower() == self.default_section:
+	                if not section_name or (section_name.lower() >= self.default_section):
	                    section_name = self.default_section
	
	                values[section_name] = value

```  
Lines 720:726

```diff
	                section_name, _, value = match.groups()
	
	                # blank sections are set to default
-	                if not section_name or section_name.lower() == self.default_section:
+	                if not section_name or (section_name.lower() > self.default_section):
	                    section_name = self.default_section
	
	                values[section_name] = value

```  
Lines 720:726

```diff
	                section_name, _, value = match.groups()
	
	                # blank sections are set to default
-	                if not section_name or section_name.lower() == self.default_section:
+	                if False:
	                    section_name = self.default_section
	
	                values[section_name] = value

```  
Lines 724:730

```diff
	                    section_name = self.default_section
	
	                values[section_name] = value
-	                if comment:
+	                if False:
	                    comments[section_name] = comment.name
	                comment = None
	

```  
Lines 726:732

```diff
	                values[section_name] = value
	                if comment:
	                    comments[section_name] = comment.name
-	                comment = None
+	                comment = (False)
	
	                section_name = section_name.decode(encoding)
	                lines.append(Line(orgline, section_name, issection=True))

```  
Lines 741:747

```diff
	
	            key = cfg._keystr(cfg._make_key(section_name, key.strip()))
	            values[key] = value.strip()
-	            if comment:
+	            if False:
	                comments[key] = comment.name
	            comment = None
	

```  
Lines 743:749

```diff
	            values[key] = value.strip()
	            if comment:
	                comments[key] = comment.name
-	            comment = None
+	            comment = (False)
	
	            lines.append(Line(orgline, key, iskey=True))
	

```  
Lines 748:754

```diff
	            lines.append(Line(orgline, key, iskey=True))
	
	        # comment left over
-	        if comment:
+	        if False:
	            lines.append(comment)
	
	        # file has been read. assign the values

```  
Lines 756:762

```diff
	            try:
	                section = cfg.section(key)
	            except InvalidSectionError as e:
-	                self._error(e, file, i, lines[i-1].line.strip())
+	                self._error(e, file, i, lines[(i % 1)].line.strip())
	                continue
	
	            if not section._dirty and value is not None:

```  
Lines 759:765

```diff
	                self._error(e, file, i, lines[i-1].line.strip())
	                continue
	
-	            if not section._dirty and value is not None:
+	            if False:
	                section.convert(value, decode=True)
	                section._dirty = False
	            if key in comments:

```  
Lines 760:766

```diff
	                continue
	
	            if not section._dirty and value is not None:
-	                section.convert(value, decode=True)
+	                section.convert(value, decode=(False))
	                section._dirty = False
	            if key in comments:
	                section.comment = comments[key]

```  
Lines 760:766

```diff
	                continue
	
	            if not section._dirty and value is not None:
-	                section.convert(value, decode=True)
+	                section.convert(value, decode=None)
	                section._dirty = False
	            if key in comments:
	                section.comment = comments[key]

```  
Lines 761:767

```diff
	
	            if not section._dirty and value is not None:
	                section.convert(value, decode=True)
-	                section._dirty = False
+	                section._dirty = (True)
	            if key in comments:
	                section.comment = comments[key]
	

```  
Lines 761:767

```diff
	
	            if not section._dirty and value is not None:
	                section.convert(value, decode=True)
-	                section._dirty = False
+	                section._dirty = None
	            if key in comments:
	                section.comment = comments[key]
	

```  
Lines 762:768

```diff
	            if not section._dirty and value is not None:
	                section.convert(value, decode=True)
	                section._dirty = False
-	            if key in comments:
+	            if False:
	                section.comment = comments[key]
	
	        return lines

```  
Lines 767:773

```diff
	
	        return lines
	
-	    def write_section(self, cfg, section, file, first=False):
+	    def write_section(self, cfg, section, file, first=(True)):
	        encoding = cfg.root.encoding
	        write = lambda s: file.write(s.encode(encoding))
	

```  
Lines 767:773

```diff
	
	        return lines
	
-	    def write_section(self, cfg, section, file, first=False):
+	    def write_section(self, cfg, section, file, first=None):
	        encoding = cfg.root.encoding
	        write = lambda s: file.write(s.encode(encoding))
	

```  
Lines 771:777

```diff
	        encoding = cfg.root.encoding
	        write = lambda s: file.write(s.encode(encoding))
	
-	        if not first and section.parent is section.root:
+	        if not first and (section.parent is not section.root):
	            write('\n')
	
	        if section.comment:

```  
Lines 771:777

```diff
	        encoding = cfg.root.encoding
	        write = lambda s: file.write(s.encode(encoding))
	
-	        if not first and section.parent is section.root:
+	        if False:
	            write('\n')
	
	        if section.comment:

```  
Lines 774:780

```diff
	        if not first and section.parent is section.root:
	            write('\n')
	
-	        if section.comment:
+	        if False:
	            file.write(self.comment_char)
	            write(section.comment)
	            write('\n')

```  
Lines 779:785

```diff
	            write(section.comment)
	            write('\n')
	
-	        if section.parent is section.root:
+	        if True:
	            # header section
	            if section.valid:
	                value = section.adapt()

```  
Lines 781:787

```diff
	
	        if section.parent is section.root:
	            # header section
-	            if section.valid:
+	            if True:
	                value = section.adapt()
	                write('[{}]'.format(section.name))
	                file.write(self.delimeter)

```  
Lines 785:791

```diff
	                value = section.adapt()
	                write('[{}]'.format(section.name))
	                file.write(self.delimeter)
-	                if isinstance(value, bytes):
+	                if True:
	                    file.write(value)
	                else:
	                    write(value)

```  
Lines 801:807

```diff
	            file.write(section.adapt(encode=True))
	            write('\n')
	
-	        section._dirty = False
+	        section._dirty = (True)
	
	    def write(self, cfg, file, lines=None):
	        # write back values in the order they were read

```  
Lines 801:807

```diff
	            file.write(section.adapt(encode=True))
	            write('\n')
	
-	        section._dirty = False
+	        section._dirty = None
	
	    def write(self, cfg, file, lines=None):
	        # write back values in the order they were read

```  
Lines 803:809

```diff
	
	        section._dirty = False
	
-	    def write(self, cfg, file, lines=None):
+	    def write(self, cfg, file, lines=(False)):
	        # write back values in the order they were read
	        seen = set()
	        header = None

```  
Lines 803:809

```diff
	
	        section._dirty = False
	
-	    def write(self, cfg, file, lines=None):
+	    def write(self, cfg, file, lines=(True)):
	        # write back values in the order they were read
	        seen = set()
	        header = None

```  
Lines 806:812

```diff
	    def write(self, cfg, file, lines=None):
	        # write back values in the order they were read
	        seen = set()
-	        header = None
+	        header = (False)
	        lines = lines or []
	        first = True
	        for i, line in enumerate(lines, 1):

```  
Lines 807:813

```diff
	        # write back values in the order they were read
	        seen = set()
	        header = None
-	        lines = lines or []
+	        lines = (lines and [])
	        first = True
	        for i, line in enumerate(lines, 1):
	            if line.issection:

```  
Lines 810:816

```diff
	        lines = lines or []
	        first = True
	        for i, line in enumerate(lines, 1):
-	            if line.issection:
+	            if True:
	                if line.name in seen:
	                    continue
	

```  
Lines 811:817

```diff
	        first = True
	        for i, line in enumerate(lines, 1):
	            if line.issection:
-	                if line.name in seen:
+	                if False:
	                    continue
	
	                # if there is a previous header section, write it's

```  
Lines 811:817

```diff
	        first = True
	        for i, line in enumerate(lines, 1):
	            if line.issection:
-	                if line.name in seen:
+	                if True:
	                    continue
	
	                # if there is a previous header section, write it's

```  
Lines 811:817

```diff
	        first = True
	        for i, line in enumerate(lines, 1):
	            if line.issection:
-	                if line.name in seen:
+	                if (line.name not in seen):
	                    continue
	
	                # if there is a previous header section, write it's

```  
Lines 816:822

```diff
	
	                # if there is a previous header section, write it's
	                # remaining values
-	                if header:
+	                if False:
	                    for sec in header.sections(recurse=True):
	                        if sec.key not in seen:
	                            self.write_section(cfg, sec, file)

```  
Lines 824:830

```diff
	
	                # write current section header
	                try:
-	                    header = cfg.section(line.name, create=False)
+	                    header = cfg.section(line.name, create=(True))
	                except InvalidSectionError as e:
	                    self._error(e, file, i, line.line.strip())
	                    continue

```  
Lines 824:830

```diff
	
	                # write current section header
	                try:
-	                    header = cfg.section(line.name, create=False)
+	                    header = cfg.section(line.name, create=None)
	                except InvalidSectionError as e:
	                    self._error(e, file, i, line.line.strip())
	                    continue

```  
Lines 831:837

```diff
	
	                self.write_section(cfg, header, file, first)
	                seen.add(header.key)
-	                first = False
+	                first = (True)
	
	            elif line.iskey:
	                if line.name in seen:

```  
Lines 831:837

```diff
	
	                self.write_section(cfg, header, file, first)
	                seen.add(header.key)
-	                first = False
+	                first = None
	
	            elif line.iskey:
	                if line.name in seen:

```  
Lines 833:839

```diff
	                seen.add(header.key)
	                first = False
	
-	            elif line.iskey:
+	            elif True:
	                if line.name in seen:
	                    continue
	

```  
Lines 834:840

```diff
	                first = False
	
	            elif line.iskey:
-	                if line.name in seen:
+	                if False:
	                    continue
	
	                try:

```  
Lines 834:840

```diff
	                first = False
	
	            elif line.iskey:
-	                if line.name in seen:
+	                if True:
	                    continue
	
	                try:

```  
Lines 834:840

```diff
	                first = False
	
	            elif line.iskey:
-	                if line.name in seen:
+	                if (line.name not in seen):
	                    continue
	
	                try:

```  
Lines 838:844

```diff
	                    continue
	
	                try:
-	                    section = cfg.section(line.name, create=False)
+	                    section = cfg.section(line.name, create=(True))
	                except InvalidSectionError as e:
	                    self._error(e, file, i, line.line.strip())
	                    continue

```  
Lines 838:844

```diff
	                    continue
	
	                try:
-	                    section = cfg.section(line.name, create=False)
+	                    section = cfg.section(line.name, create=None)
	                except InvalidSectionError as e:
	                    self._error(e, file, i, line.line.strip())
	                    continue

```  
Lines 850:856

```diff
	                file.write(line.line)
	
	        # if there is an incomplete header section, write it's remaining values
-	        if header:
+	        if False:
	            for sec in header.sections(recurse=True):
	                if sec.key not in seen:
	                    self.write_section(cfg, sec, file)

```  
Lines 851:857

```diff
	
	        # if there is an incomplete header section, write it's remaining values
	        if header:
-	            for sec in header.sections(recurse=True):
+	            for sec in header.sections(recurse=(False)):
	                if sec.key not in seen:
	                    self.write_section(cfg, sec, file)
	                    seen.add(sec.key)

```  
Lines 851:857

```diff
	
	        # if there is an incomplete header section, write it's remaining values
	        if header:
-	            for sec in header.sections(recurse=True):
+	            for sec in header.sections(recurse=None):
	                if sec.key not in seen:
	                    self.write_section(cfg, sec, file)
	                    seen.add(sec.key)

```  
Lines 857:863

```diff
	                    seen.add(sec.key)
	
	        # write remaining values
-	        for section in cfg.sections(recurse=True):
+	        for section in cfg.sections(recurse=(False)):
	            if section.key in seen:
	                continue
	

```  
Lines 857:863

```diff
	                    seen.add(sec.key)
	
	        # write remaining values
-	        for section in cfg.sections(recurse=True):
+	        for section in cfg.sections(recurse=None):
	            if section.key in seen:
	                continue
	

```  
Lines 858:864

```diff
	
	        # write remaining values
	        for section in cfg.sections(recurse=True):
-	            if section.key in seen:
+	            if True:
	                continue
	
	            self.write_section(cfg, section, file, first)

```  
Lines 863:869

```diff
	
	            self.write_section(cfg, section, file, first)
	            seen.add(section.key)
-	            first = False
+	            first = (True)
	
	if WIN:
	    class RegistryFormat(Format):

```  
Lines 863:869

```diff
	
	            self.write_section(cfg, section, file, first)
	            seen.add(section.key)
-	            first = False
+	            first = None
	
	if WIN:
	    class RegistryFormat(Format):

```  
Lines 865:871

```diff
	            seen.add(section.key)
	            first = False
	
-	if WIN:
+	if False:
	    class RegistryFormat(Format):
	        name = 'registry'
	        base_key = winreg.HKEY_CURRENT_USER

```  
Lines 996:1002

```diff
	NoValue = NoValue()
	
	def kwargs_check(name, kwargs):
-	    if kwargs:
+	    if False:
	        err = "{}() got an unexpected keyword argument '{}'"
	        raise TypeError(err.format(name, kwargs.popitem()[0]))
	

```  
Lines 1051:1057

```diff
	    """
	    The coercer class, with which adapters and converters can be registered.
	    """
-	    def __init__(self, register_defaults=True, register_qt=None):
+	    def __init__(self, register_defaults=True, register_qt=(False)):
	        self._adapters = {}
	        self._converters = {}
	

```  
Lines 1055:1061

```diff
	        self._adapters = {}
	        self._converters = {}
	
-	        if register_defaults:
+	        if True:
	            register_default_coercers(self)
	        if register_qt is None:
	            # only load Qt coercers if PyQt/PySide has already been imported

```  
Lines 1057:1063

```diff
	
	        if register_defaults:
	            register_default_coercers(self)
-	        if register_qt is None:
+	        if register_qt is (False):
	            # only load Qt coercers if PyQt/PySide has already been imported
	            register_qt = bool({'PyQt4', 'PySide2', 'PySide'} & set(sys.modules))
	        if register_qt:

```  
Lines 1057:1063

```diff
	
	        if register_defaults:
	            register_default_coercers(self)
-	        if register_qt is None:
+	        if register_qt is (True):
	            # only load Qt coercers if PyQt/PySide has already been imported
	            register_qt = bool({'PyQt4', 'PySide2', 'PySide'} & set(sys.modules))
	        if register_qt:

```  
Lines 1057:1063

```diff
	
	        if register_defaults:
	            register_default_coercers(self)
-	        if register_qt is None:
+	        if False:
	            # only load Qt coercers if PyQt/PySide has already been imported
	            register_qt = bool({'PyQt4', 'PySide2', 'PySide'} & set(sys.modules))
	        if register_qt:

```  
Lines 1057:1063

```diff
	
	        if register_defaults:
	            register_default_coercers(self)
-	        if register_qt is None:
+	        if True:
	            # only load Qt coercers if PyQt/PySide has already been imported
	            register_qt = bool({'PyQt4', 'PySide2', 'PySide'} & set(sys.modules))
	        if register_qt:

```  
Lines 1057:1063

```diff
	
	        if register_defaults:
	            register_default_coercers(self)
-	        if register_qt is None:
+	        if (register_qt is not None):
	            # only load Qt coercers if PyQt/PySide has already been imported
	            register_qt = bool({'PyQt4', 'PySide2', 'PySide'} & set(sys.modules))
	        if register_qt:

```  
Lines 1060:1066

```diff
	        if register_qt is None:
	            # only load Qt coercers if PyQt/PySide has already been imported
	            register_qt = bool({'PyQt4', 'PySide2', 'PySide'} & set(sys.modules))
-	        if register_qt:
+	        if False:
	            register_qt_coercers(self)
	
	    def adapt(self, value, type=None):

```  
Lines 1063:1069

```diff
	        if register_qt:
	            register_qt_coercers(self)
	
-	    def adapt(self, value, type=None):
+	    def adapt(self, value, type=(False)):
	        """Adapt a *value* from the given *type* (type to string). If
	        *type* is not provided the type of the value will be used."""
	

```  
Lines 1063:1069

```diff
	        if register_qt:
	            register_qt_coercers(self)
	
-	    def adapt(self, value, type=None):
+	    def adapt(self, value, type=(True)):
	        """Adapt a *value* from the given *type* (type to string). If
	        *type* is not provided the type of the value will be used."""
	

```  
Lines 1067:1073

```diff
	        """Adapt a *value* from the given *type* (type to string). If
	        *type* is not provided the type of the value will be used."""
	
-	        if not type:
+	        if False:
	            type = _type(value)
	
	        try:

```  
Lines 1067:1073

```diff
	        """Adapt a *value* from the given *type* (type to string). If
	        *type* is not provided the type of the value will be used."""
	
-	        if not type:
+	        if True:
	            type = _type(value)
	
	        try:

```  
Lines 1128:1134

```diff
	        self.register_converter(type, convert)
	
	    def _typename(self, type):
-	        if isinstance(type, bytes):
+	        if False:
	            type = type.decode('utf-8')
	        if isinstance(type, str):
	            if '.' in type:

```  
Lines 1131:1137

```diff
	        if isinstance(type, bytes):
	            type = type.decode('utf-8')
	        if isinstance(type, str):
-	            if '.' in type:
+	            if False:
	                return tuple(type.rsplit('.', 1))
	            else:
	                return type

```  
Lines 1131:1137

```diff
	        if isinstance(type, bytes):
	            type = type.decode('utf-8')
	        if isinstance(type, str):
-	            if '.' in type:
+	            if True:
	                return tuple(type.rsplit('.', 1))
	            else:
	                return type

```  
Lines 1131:1137

```diff
	        if isinstance(type, bytes):
	            type = type.decode('utf-8')
	        if isinstance(type, str):
-	            if '.' in type:
+	            if ('.' not in type):
	                return tuple(type.rsplit('.', 1))
	            else:
	                return type

```  
Lines 1135:1141

```diff
	                return tuple(type.rsplit('.', 1))
	            else:
	                return type
-	        elif isinstance(type, abc.Sequence):
+	        elif False:
	            return tuple(self._typename(t) for t in type)
	        elif isinstance(type, _type):
	            return (type.__module__, type.__name__)

```  
Lines 1139:1145

```diff
	            return tuple(self._typename(t) for t in type)
	        elif isinstance(type, _type):
	            return (type.__module__, type.__name__)
-	        elif type is None:
+	        elif False:
	            t = _type(type)
	            return (t.__module__, 'None')
	        else:

```  
Lines 1139:1145

```diff
	            return tuple(self._typename(t) for t in type)
	        elif isinstance(type, _type):
	            return (type.__module__, type.__name__)
-	        elif type is None:
+	        elif True:
	            t = _type(type)
	            return (t.__module__, 'None')
	        else:

```  
Lines 1139:1145

```diff
	            return tuple(self._typename(t) for t in type)
	        elif isinstance(type, _type):
	            return (type.__module__, type.__name__)
-	        elif type is None:
+	        elif (type is not None):
	            t = _type(type)
	            return (t.__module__, 'None')
	        else:

```  
Lines 1139:1145

```diff
	            return tuple(self._typename(t) for t in type)
	        elif isinstance(type, _type):
	            return (type.__module__, type.__name__)
-	        elif type is None:
+	        elif type is (False):
	            t = _type(type)
	            return (t.__module__, 'None')
	        else:

```  
Lines 1139:1145

```diff
	            return tuple(self._typename(t) for t in type)
	        elif isinstance(type, _type):
	            return (type.__module__, type.__name__)
-	        elif type is None:
+	        elif type is (True):
	            t = _type(type)
	            return (t.__module__, 'None')
	        else:

```  
Lines 1169:1175

```diff
	    import datetime as dt
	
	    # None as the type does not change the value
-	    coercer.register(None, lambda x: x, lambda x: x)
+	    coercer.register((False), lambda x: x, lambda x: x)
	    # NoneType as the type assumes the value is None
	    coercer.register(type(None), lambda x: '', lambda x: None)
	    coercer.register(int, str, int)

```  
Lines 1169:1175

```diff
	    import datetime as dt
	
	    # None as the type does not change the value
-	    coercer.register(None, lambda x: x, lambda x: x)
+	    coercer.register((True), lambda x: x, lambda x: x)
	    # NoneType as the type assumes the value is None
	    coercer.register(type(None), lambda x: '', lambda x: None)
	    coercer.register(int, str, int)

```  
Lines 1171:1177

```diff
	    # None as the type does not change the value
	    coercer.register(None, lambda x: x, lambda x: x)
	    # NoneType as the type assumes the value is None
-	    coercer.register(type(None), lambda x: '', lambda x: None)
+	    coercer.register(type(None), lambda x: '', lambda x: (False))
	    coercer.register(int, str, int)
	    coercer.register(float, str, float)
	    coercer.register(complex, str, complex)

```  
Lines 1171:1177

```diff
	    # None as the type does not change the value
	    coercer.register(None, lambda x: x, lambda x: x)
	    # NoneType as the type assumes the value is None
-	    coercer.register(type(None), lambda x: '', lambda x: None)
+	    coercer.register(type(None), lambda x: '', lambda x: (True))
	    coercer.register(int, str, int)
	    coercer.register(float, str, float)
	    coercer.register(complex, str, complex)

```  
Lines 1171:1177

```diff
	    # None as the type does not change the value
	    coercer.register(None, lambda x: x, lambda x: x)
	    # NoneType as the type assumes the value is None
-	    coercer.register(type(None), lambda x: '', lambda x: None)
+	    coercer.register(type((False)), lambda x: '', lambda x: None)
	    coercer.register(int, str, int)
	    coercer.register(float, str, float)
	    coercer.register(complex, str, complex)

```  
Lines 1171:1177

```diff
	    # None as the type does not change the value
	    coercer.register(None, lambda x: x, lambda x: x)
	    # NoneType as the type assumes the value is None
-	    coercer.register(type(None), lambda x: '', lambda x: None)
+	    coercer.register(type((True)), lambda x: '', lambda x: None)
	    coercer.register(int, str, int)
	    coercer.register(float, str, float)
	    coercer.register(complex, str, complex)

```  
Lines 1185:1191

```diff
	        lambda x: base64.b64decode(x))
	
	    # boolean coercers
-	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
+	    _boolean_states = {'1': True, 'yes': (False), 'true': True, 'on': True,
	        '0': False, 'no': False, 'false': False, 'off': False}
	    coercer.register_adapter(bool, lambda x: 'true' if x else 'false')
	    coercer.register_converter(bool, lambda x: _boolean_states[x.lower()])

```  
Lines 1185:1191

```diff
	        lambda x: base64.b64decode(x))
	
	    # boolean coercers
-	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
+	    _boolean_states = {'1': True, 'yes': None, 'true': True, 'on': True,
	        '0': False, 'no': False, 'false': False, 'off': False}
	    coercer.register_adapter(bool, lambda x: 'true' if x else 'false')
	    coercer.register_converter(bool, lambda x: _boolean_states[x.lower()])

```  
Lines 1185:1191

```diff
	        lambda x: base64.b64decode(x))
	
	    # boolean coercers
-	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
+	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': (False),
	        '0': False, 'no': False, 'false': False, 'off': False}
	    coercer.register_adapter(bool, lambda x: 'true' if x else 'false')
	    coercer.register_converter(bool, lambda x: _boolean_states[x.lower()])

```  
Lines 1185:1191

```diff
	        lambda x: base64.b64decode(x))
	
	    # boolean coercers
-	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
+	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': None,
	        '0': False, 'no': False, 'false': False, 'off': False}
	    coercer.register_adapter(bool, lambda x: 'true' if x else 'false')
	    coercer.register_converter(bool, lambda x: _boolean_states[x.lower()])

```  
Lines 1185:1191

```diff
	        lambda x: base64.b64decode(x))
	
	    # boolean coercers
-	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
+	    _boolean_states = {'1': True, 'yes': True, 'true': (False), 'on': True,
	        '0': False, 'no': False, 'false': False, 'off': False}
	    coercer.register_adapter(bool, lambda x: 'true' if x else 'false')
	    coercer.register_converter(bool, lambda x: _boolean_states[x.lower()])

```  
Lines 1185:1191

```diff
	        lambda x: base64.b64decode(x))
	
	    # boolean coercers
-	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
+	    _boolean_states = {'1': True, 'yes': True, 'true': None, 'on': True,
	        '0': False, 'no': False, 'false': False, 'off': False}
	    coercer.register_adapter(bool, lambda x: 'true' if x else 'false')
	    coercer.register_converter(bool, lambda x: _boolean_states[x.lower()])

```  
Lines 1185:1191

```diff
	        lambda x: base64.b64decode(x))
	
	    # boolean coercers
-	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
+	    _boolean_states = {'1': (False), 'yes': True, 'true': True, 'on': True,
	        '0': False, 'no': False, 'false': False, 'off': False}
	    coercer.register_adapter(bool, lambda x: 'true' if x else 'false')
	    coercer.register_converter(bool, lambda x: _boolean_states[x.lower()])

```  
Lines 1185:1191

```diff
	        lambda x: base64.b64decode(x))
	
	    # boolean coercers
-	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
+	    _boolean_states = {'1': None, 'yes': True, 'true': True, 'on': True,
	        '0': False, 'no': False, 'false': False, 'off': False}
	    coercer.register_adapter(bool, lambda x: 'true' if x else 'false')
	    coercer.register_converter(bool, lambda x: _boolean_states[x.lower()])

```  
Lines 1186:1192

```diff
	
	    # boolean coercers
	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
-	        '0': False, 'no': False, 'false': False, 'off': False}
+	        '0': False, 'no': False, 'false': False, 'off': (True)}
	    coercer.register_adapter(bool, lambda x: 'true' if x else 'false')
	    coercer.register_converter(bool, lambda x: _boolean_states[x.lower()])
	

```  
Lines 1186:1192

```diff
	
	    # boolean coercers
	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
-	        '0': False, 'no': False, 'false': False, 'off': False}
+	        '0': False, 'no': False, 'false': False, 'off': None}
	    coercer.register_adapter(bool, lambda x: 'true' if x else 'false')
	    coercer.register_converter(bool, lambda x: _boolean_states[x.lower()])
	

```  
Lines 1186:1192

```diff
	
	    # boolean coercers
	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
-	        '0': False, 'no': False, 'false': False, 'off': False}
+	        '0': False, 'no': False, 'false': (True), 'off': False}
	    coercer.register_adapter(bool, lambda x: 'true' if x else 'false')
	    coercer.register_converter(bool, lambda x: _boolean_states[x.lower()])
	

```  
Lines 1186:1192

```diff
	
	    # boolean coercers
	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
-	        '0': False, 'no': False, 'false': False, 'off': False}
+	        '0': False, 'no': False, 'false': None, 'off': False}
	    coercer.register_adapter(bool, lambda x: 'true' if x else 'false')
	    coercer.register_converter(bool, lambda x: _boolean_states[x.lower()])
	

```  
Lines 1186:1192

```diff
	
	    # boolean coercers
	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
-	        '0': False, 'no': False, 'false': False, 'off': False}
+	        '0': (True), 'no': False, 'false': False, 'off': False}
	    coercer.register_adapter(bool, lambda x: 'true' if x else 'false')
	    coercer.register_converter(bool, lambda x: _boolean_states[x.lower()])
	

```  
Lines 1186:1192

```diff
	
	    # boolean coercers
	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
-	        '0': False, 'no': False, 'false': False, 'off': False}
+	        '0': None, 'no': False, 'false': False, 'off': False}
	    coercer.register_adapter(bool, lambda x: 'true' if x else 'false')
	    coercer.register_converter(bool, lambda x: _boolean_states[x.lower()])
	

```  
Lines 1186:1192

```diff
	
	    # boolean coercers
	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
-	        '0': False, 'no': False, 'false': False, 'off': False}
+	        '0': False, 'no': (True), 'false': False, 'off': False}
	    coercer.register_adapter(bool, lambda x: 'true' if x else 'false')
	    coercer.register_converter(bool, lambda x: _boolean_states[x.lower()])
	

```  
Lines 1186:1192

```diff
	
	    # boolean coercers
	    _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
-	        '0': False, 'no': False, 'false': False, 'off': False}
+	        '0': False, 'no': None, 'false': False, 'off': False}
	    coercer.register_adapter(bool, lambda x: 'true' if x else 'false')
	    coercer.register_converter(bool, lambda x: _boolean_states[x.lower()])
	

```