import pytest
from presidio_anonymizer.entities import  EngineResult, OperatorResult
from presidio_anonymizer.sample import  sample_run_anonymizer


@pytest.mark.parametrize(
    "text, start, end,expected_result",
    [
        ("My name is Bond.",11,15,
        {
            "text": "My name is BIP.",
            "items":  {'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}
        })
    ],
)
def test_sample_run_anonymizer(text,start,end,expected_result):
    result = sample_run_anonymizer(text,start,end)
    expected_engine_result = create_engine_result(expected_result)
    assert expected_engine_result == result

def create_engine_result(json):
    operation_result:OperatorResult = OperatorResult.from_json(json["items"])
    result = EngineResult(text=json["text"],items = [operation_result])
    return result

