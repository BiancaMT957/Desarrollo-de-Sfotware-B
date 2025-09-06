import sys
import json

def summarize(nums):
    """Recibe una lista de números y devuelve count, sum y avg"""
    if not nums:
        raise ValueError("La lista no puede estar vacía")

    count = len(nums)
    total = sum(nums)
    avg = total / count
    return {"count": count, "sum": total, "avg": avg}


def main():
    if len(sys.argv) != 2:
        print("Uso: python -m app \"1,2,3\"")
        sys.exit(1)

    try:
        # Convertir la cadena "1,2,3" en lista de enteros
        nums = [float(x) for x in sys.argv[1].split(",")]
        result = summarize(nums)
        print(json.dumps(result))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
