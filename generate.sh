#!/bin/bash
# OpenVIP SDK Generator
# Usage: ./generate.sh <openapi-spec-url-or-path> [--only <language>]
#
# Examples:
#   ./generate.sh https://raw.githubusercontent.com/open-voice-input/spec/main/bindings/http/openapi.yaml
#   ./generate.sh /path/to/openapi.yaml
#   ./generate.sh https://... --only python

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# Default spec URL
DEFAULT_SPEC="https://raw.githubusercontent.com/open-voice-input/spec/main/bindings/http/openapi.yaml"

# Parse arguments
SPEC="${1:-$DEFAULT_SPEC}"
ONLY=""

shift || true
while [[ $# -gt 0 ]]; do
    case $1 in
        --only)
            ONLY="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

echo "OpenVIP SDK Generator"
echo "====================="
echo ""
echo "Spec: $SPEC"
echo ""

# Check Docker
if ! command -v docker &> /dev/null; then
    echo "Error: Docker is required but not installed."
    echo "Install from: https://www.docker.com/"
    exit 1
fi

# Prepare spec path for Docker
if [[ "$SPEC" == http* ]]; then
    # Download spec to temp file
    TEMP_SPEC="$SCRIPT_DIR/.openapi-spec.yaml"
    echo "Downloading spec..."
    curl -sL "$SPEC" -o "$TEMP_SPEC"
    DOCKER_SPEC="/local/.openapi-spec.yaml"
else
    # Local file - use absolute path
    TEMP_SPEC=""
    if [[ "$SPEC" == /* ]]; then
        DOCKER_SPEC="/local/$(basename "$SPEC")"
        cp "$SPEC" "$SCRIPT_DIR/$(basename "$SPEC")"
    else
        DOCKER_SPEC="/local/$SPEC"
    fi
fi

# Pull latest generator
echo "Pulling openapi-generator-cli..."
docker pull openapitools/openapi-generator-cli:latest

generate() {
    local lang=$1
    local generator=$2
    local package=$3
    local extra=${4:-}

    if [[ -n "$ONLY" && "$ONLY" != "$lang" ]]; then
        return
    fi

    echo ""
    echo "Generating: $lang ($generator)..."
    rm -rf "$lang"

    docker run --rm \
        -v "$SCRIPT_DIR:/local" \
        openapitools/openapi-generator-cli:latest generate \
        -i "$DOCKER_SPEC" \
        -g "$generator" \
        -o "/local/$lang" \
        --package-name "$package" \
        $extra

    echo "  → $lang/"
}

echo ""
echo "=== GENERATING SDKs ==="

generate "python" "python" "openvip"
generate "dotnet" "csharp" "OpenVip"

# Future SDKs (uncomment as needed)
# generate "typescript" "typescript-fetch" "openvip" "--additional-properties=npmName=openvip"
# generate "go" "go" "openvip"
# generate "rust" "rust" "openvip"
# generate "swift" "swift6" "OpenVip" "--additional-properties=projectName=OpenVip"
# generate "kotlin" "kotlin" "org.openvip"
# generate "java" "java" "org.openvip"

# Cleanup
if [[ -n "$TEMP_SPEC" ]]; then
    rm -f "$TEMP_SPEC"
fi

echo ""
echo "Done!"
echo ""
echo "Generated SDKs:"
ls -d */ 2>/dev/null | grep -v '^\.' | sed 's/^/  /'
echo ""
echo "To add more languages, edit this script."
