#!/usr/bin/env python3
"""
Fetch a YouTube video transcript and save it locally for private research use.

Workflow (see tools/youtube_transcript_collector_plan.md):
  1. Accept a YouTube URL or bare video ID from the command line.
  2. Normalize the input to an 11-character video ID.
  3. Request an English caption track via youtube-transcript-api.
  4. Write plain text to research/youtube-transcripts/raw/{video_id}.txt
  5. Summarize into structured notes separately — do not commit full transcripts publicly.

Usage:
  python tools/youtube_transcript_collector.py "https://www.youtube.com/watch?v=VIDEO_ID"
  python tools/youtube_transcript_collector.py VIDEO_ID
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from youtube_transcript_api import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
    YouTubeTranscriptApi,
)

# Raw transcripts stay in raw/; structured research notes live one level up.
REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "research" / "youtube-transcripts" / "raw"

# YouTube video IDs are 11 characters: letters, digits, underscore, hyphen.
VIDEO_ID_PATTERN = re.compile(r"^[a-zA-Z0-9_-]{11}$")

# Common URL shapes we accept when the user passes a link instead of an ID.
URL_PATTERNS = (
    re.compile(
        r"(?:youtube\.com/watch\?(?:[^&\s]+&)*v=|youtube\.com/watch\?v=)"
        r"([a-zA-Z0-9_-]{11})"
    ),
    re.compile(r"youtu\.be/([a-zA-Z0-9_-]{11})"),
    re.compile(r"youtube\.com/embed/([a-zA-Z0-9_-]{11})"),
    re.compile(r"youtube\.com/shorts/([a-zA-Z0-9_-]{11})"),
    re.compile(r"youtube\.com/live/([a-zA-Z0-9_-]{11})"),
)


def extract_video_id(value: str) -> str:
    """
    Turn a YouTube URL or bare ID into a canonical 11-character video ID.

    Raises ValueError when the input cannot be parsed.
    """
    candidate = value.strip()
    if not candidate:
        raise ValueError("Input is empty. Provide a YouTube URL or video ID.")

    if VIDEO_ID_PATTERN.fullmatch(candidate):
        return candidate

    for pattern in URL_PATTERNS:
        match = pattern.search(candidate)
        if match:
            return match.group(1)

    raise ValueError(
        "Could not extract a valid YouTube video ID. "
        "Use a watch URL, youtu.be link, or an 11-character video ID."
    )


def fetch_english_transcript(video_id: str):
    """
    Request an English transcript track via youtube-transcript-api (v1.0+ instance API).

    Tries en, en-US, and en-GB in order. Manual and auto-generated English captions
    are both accepted when the library can find them.
    """
    api = YouTubeTranscriptApi()
    return api.fetch(video_id, languages=["en", "en-US", "en-GB"])


def transcript_to_text(fetched_transcript) -> str:
    """Join caption snippets into readable plain text (one snippet per line)."""
    return "\n".join(
        snippet.text.strip()
        for snippet in fetched_transcript.snippets
        if snippet.text.strip()
    )


def save_transcript(video_id: str, text: str) -> Path:
    """Write transcript text under research/youtube-transcripts/raw/."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / f"{video_id}.txt"
    output_path.write_text(text, encoding="utf-8")
    return output_path


def collect_transcript(video_url_or_id: str) -> Path:
    """
    End-to-end collection: parse ID, fetch English transcript, save locally.

    Returns the path to the saved .txt file on success.
    """
    video_id = extract_video_id(video_url_or_id)
    fetched = fetch_english_transcript(video_id)
    text = transcript_to_text(fetched)

    if not text.strip():
        raise NoTranscriptFound(video_id)

    return save_transcript(video_id, text)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Collect a YouTube English transcript for local B2B SaaS SEO research."
    )
    parser.add_argument(
        "video",
        help="YouTube video URL (watch, youtu.be, shorts) or 11-character video ID",
    )
    args = parser.parse_args()

    try:
        output_path = collect_transcript(args.video)
    except ValueError as exc:
        print(f"FAILURE: Invalid input — {exc}", file=sys.stderr)
        return 1
    except TranscriptsDisabled:
        print(
            "FAILURE: Transcripts are disabled for this video. "
            "Use manual notes (see tools/youtube_transcript_collector_plan.md).",
            file=sys.stderr,
        )
        return 1
    except NoTranscriptFound:
        print(
            "FAILURE: No English transcript found for this video. "
            "Try manual collection or another video from the same expert.",
            file=sys.stderr,
        )
        return 1
    except VideoUnavailable:
        print(
            "FAILURE: Video is unavailable (private, removed, or region-blocked).",
            file=sys.stderr,
        )
        return 1
    except Exception as exc:  # noqa: BLE001 — surface unexpected errors clearly for beginners
        print(f"FAILURE: Unexpected error — {exc}", file=sys.stderr)
        return 1

    print(f"SUCCESS: Transcript saved to {output_path}")
    print(
        "Next step: summarize into a research note in research/youtube-transcripts/ "
        "(do not commit full raw transcripts to the public repo if avoidable)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
