import pytest
from presidio_anonymizer.sample import  sample_run_anonymizer
import json

@pytest.mark.parametrize(
    "text, start, end,expected_result",
    [
        ("My name is Bond.",11,15,
        {
            "text": "My name is BIP.",
            "items":  [
                {'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}
            ]
        })
    ],
)
def test_sample_run_anonymizer(text,start,end,expected_result):
    result = sample_run_anonymizer(text,start,end)
    assert result.text == expected_result["text"]
    assert result.items[0].start == expected_result["items"][0]["start"]
    assert result.items[0].end == expected_result["items"][0]["end"]
    assert len(result.to_json()) == len(json.dumps(expected_result))