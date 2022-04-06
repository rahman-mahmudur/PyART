class CaseInsensitiveDict(dict):

    def _lower_keys(self):
        return [k.lower() for k in self.keys()]

    def __contains__(self, key):

    def __getitem__(self, key):
        if key in self:
            reveal_type(self)