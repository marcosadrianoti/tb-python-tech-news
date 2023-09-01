from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest
from unittest.mock import Mock, patch


def test_reading_plan_group_news():
    reading_plan_service = ReadingPlanService()
    with pytest.raises(
        ValueError,
        match="Valor 'available_time' deve ser maior que zero",
    ):
        reading_plan_service.group_news_for_available_time(0)

    news_mock = [
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia 1",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 4,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia 2",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 5,
            "summary": "Algo muito bacana aconteceu",
            "category": "Tecnologia",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia 3",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 15,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia 4",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 20,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        }
    ]

    mock_find_news = Mock(return_value=news_mock)
    with patch("tech_news.analyzer.reading_plan.find_news", mock_find_news):
        result = reading_plan_service.group_news_for_available_time(10)
        assert len(result['readable']) == 1
        assert len(result['readable'][0]['chosen_news']) == 2
        assert result['readable'][0]['chosen_news'][0] == ('Notícia 1', 4)
        assert result['readable'][0]['chosen_news'][1] == ('Notícia 2', 5)
        assert result['readable'][0]['unfilled_time'] == 1
        assert len(result['unreadable']) == 2
        assert result['unreadable'][0] == ('Notícia 3', 15)
        assert result['unreadable'][1] == ('Notícia 4', 20)
