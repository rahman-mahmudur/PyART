from typing import Dict, MutableMapping, Mapping

from allennlp.data.fields.field import DataArray, Field
from allennlp.data.vocabulary import Vocabulary


class Instance(Mapping[str, Field]):

    __slots__ = ["fields", "indexed"]

    def __init__(self, fields: MutableMapping[str, Field]) -> None:
        self.fields = fields
        self.indexed = False

    def __getitem__(self, key: str) -> Field:
        return self.fields[key]

    def __iter__(self):
        return iter(self.fields)

    def __len__(self) -> int:
        return len(self.fields)

    def add_field(self, field_name: str, field: Field, vocab: Vocabulary = None) -> None:
        self.fields[field_name] = field
        if self.indexed:
            field.index(vocab)

    def count_vocab_items(self, counter: Dict[str, Dict[str, int]]):
        for field in self.fields.values():
            field.count_vocab_items(counter)

    def index_fields(self, vocab: Vocabulary) -> None:
        if not self.indexed:
            self.indexed = True
            for field in self.fields.values():
                field.index(vocab)

    def get_padding_lengths(self) -> Dict[str, Dict[str, int]]:
        lengths = {}
        for field_name, field in self.fields.items():
            lengths[field_name] = field.get_padding_lengths()
        return lengths

    def as_tensor_dict(
        self, padding_lengths: Dict[str, Dict[str, int]] = None
    ) -> Dict[str, DataArray]:
        padding_lengths = padding_lengths or self.get_padding_lengths()
        tensors = {}
        for field_name, field in self.fields.items():
            tensors[field_name] = field.as_tensor(padding_lengths[field_name])
        return tensors

    def __str__(self) -> str:
        base_string = "Instance with fields:\n"
        return " ".join(
            [base_string] + [f"\t {name}: {field} \n" for name, field in self.fields.items()]
        )

    def duplicate(self) -> "Instance":
        reveal_type(field)