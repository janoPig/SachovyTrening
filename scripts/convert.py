import re
import sys
import argparse

def pgn_to_lichess_link(pgn_path):
    with open(pgn_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(r'\[.*?\]\s*', '', content)
    content = re.sub(r'\d+\.(\.\.)?', '', content)
    content = re.sub(r'\{.*?\}', '', content)
    moves = content.strip().split()
    cleaned_moves = [re.sub(r'[+x#]', '', move) for move in moves]
    move_str = '_'.join(cleaned_moves)

    lichess_url = f'https://lichess.org/analysis/pgn/{move_str}'
    return lichess_url

def main():
    parser = argparse.ArgumentParser(description='Konvertuj PGN súbor na Lichess game import link.')
    parser.add_argument('pgn_path', help='Cesta k PGN súboru')
    args = parser.parse_args()

    link = pgn_to_lichess_link(args.pgn_path)
    print('Lichess link:', link)

if __name__ == '__main__':
    main()
