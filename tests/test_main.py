import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import mock_feedback, call_qwen

def test_mock_feedback_returns_string():
    result = mock_feedback("测试问题")
    assert isinstance(result, str)
    assert "总分" in result

def test_call_qwen_without_key():
    result = call_qwen("system", "user")
    assert isinstance(result, str)
    assert len(result) > 0