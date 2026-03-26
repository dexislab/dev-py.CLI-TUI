def main():
    import argparse

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="MCP Server")


    parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio",
                        help="Transport to use (stdio or sse, default: stdio)")

    parser.add_argument("--port", type=int,
                        help="Port to use (overrides MCP_PORT environment variable)")

    args = parser.parse_args()

    print(f"OPTIONS: transport -> {args.transport}, port -> {args.port}")



if __name__ == "__main__":
    main()
