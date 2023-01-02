import numpy as np


def test_numpy_array_basic_algebra() -> None:
    """Basic algebra on a numpy array.

    en: Example of basic algebra on a numpy array
    ja: numpy の配列に対する基本的な代数演算の見本
    """

    # en: Comparison operators (1): all elements are equal
    # ja: array_equal() を使うと配列全体の等価性を行う
    assert np.array_equal(np.array([1, 2, 3]), np.array([1, 2, 3]))

    # en: Comparison operators (2): == is element-wise comparison
    # ja: == だけでは配列全体の等価性ではなく各成分の等価性の比較結果の配列が返る
    x = np.array([1, 2, 3]) == np.array([1, 2, 3])
    y = np.array([True, True, True])
    assert np.array_equal(x, y)

    # en: Comparison operators (3): all() is same as array_equal()
    # ja: all() も array_equal() と同様に配列全体の等価性を行う
    assert (np.array([1, 2, 3]) == np.array([1, 2, 3])).all()

    # en: Addition
    # ja: 足し算
    assert (
        np.array([1, 2, 3]) + np.array([1, 2, 3]) == np.array([2, 4, 6])
    ).all()

    # en: Subtraction
    # ja: 引き算
    assert (
        np.array([4, 5, 6]) - np.array([1, 2, 3]) == np.array([3, 3, 3])
    ).all()

    # en: Multiplication
    # ja: 各成分の掛け算
    assert (
        np.array([1, 2, 3]) * np.array([2, 3, 4]) == np.array([2, 6, 12])
    ).all()

    # en: Division
    # ja: 各成分の割り算
    assert (
        np.array([4, 5, 6]) / np.array([1, 2, 3]) == np.array([4, 2.5, 2])
    ).all()

    # en: Dot product
    # ja: 内積
    assert np.dot(np.array([1, 2, 3]), np.array([1, 2, 3])) == 14

    # en: Cross product
    # ja: 外積
    assert (
        np.cross(np.array([1, 2, 3]), np.array([4, 5, 6]))
        == np.array([-3, 6, -3])
    ).all()

    # en: Element-wise power: element-wise power
    # ja: 各成分ごとのべき乗
    assert (
        np.array([1, 2, 3]) ** np.array([2, 3, 4]) == np.array([1, 8, 81])
    ).all()

    # en: Element-wise power (2): scalar power
    # ja: スカラーのべき乗
    assert (np.array([1, 2, 3]) ** 2 == np.array([1, 4, 9])).all()


def test_numpy_types() -> None:
    """Types of numpy arrays.

    en: Example of types of numpy arrays
    ja: numpy の配列の型の見本
    """

    # int64
    x = np.array(
        [1, 2, 3, 4, 5]
    )  # en: Python's int list is converted to int64 by default
    assert x.dtype == np.int64
    assert x.size == 5, "array size is 5"
    assert x.itemsize == 8, "int64 is 8 bytes"
    assert x.size * x.itemsize == 40, "array byte size is 40"

    # float64
    x = np.array(
        [1.0, 2.0, 3.0, 4.0, 5.0]
    )  # en: Python's float list is converted to float64 by default
    assert x.dtype == np.float64
    assert x.size == 5, "size is 5"
    assert x.itemsize == 8, "float64 is 8 bytes"
    assert x.size * x.itemsize == 40, "array byte size is 40"

    # complex128
    x = np.array([1.0 + 1.0j, 2.0 + 2.0j, 3.0 + 3.0j, 4.0 + 4.0j, 5.0 + 5.0j])
    assert x.dtype == np.complex128
    assert x.size == 5, "size is 5"
    assert x.itemsize == 16, "complex128 is 16 bytes"
    assert x.size * x.itemsize == 80, "array byte size is 80"

    # int32
    x = np.array(
        [1, 2, 3, 4, 5], dtype=np.int32
    )  # explicit type specification is required
    assert x.dtype == np.int32
    assert x.size == 5, "size is 5"
    assert x.itemsize == 4, "int32 is 4 bytes"
    assert x.size * x.itemsize == 20, "array byte size is 20"

    # float32
    x = np.array(
        [1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float32
    )  # explicit type specification is required
    assert x.dtype == np.float32
    assert x.size == 5, "size is 5"
    assert x.itemsize == 4, "float32 is 4 bytes"
    assert x.size * x.itemsize == 20, "array byte size is 20"

    # complex64
    x = np.array(
        [1.0 + 1.0j, 2.0 + 2.0j, 3.0 + 3.0j, 4.0 + 4.0j, 5.0 + 5.0j],
        dtype=np.complex64,
    )  # explicit type specification is required
    assert x.dtype == np.complex64
    assert x.size == 5, "size is 5"
    assert x.itemsize == 8, "complex64 is 8 bytes"
    assert x.size * x.itemsize == 40, "array byte size is 40"

    # mixed
    x = np.array(
        [1, 2, 3, 4, 5.0]
    )  # en: mixed int and float is converted to float
    assert x.dtype == np.float64
    assert x.size == 5, "size is 5"
    assert x.itemsize == 8, "float64 is 8 bytes"
    assert x.size * x.itemsize == 40, "array byte size is 40"

    # string (fixed length)
    x = np.array(["a", "b", "c", "d", "e"])
    assert x.dtype == np.dtype("U1")
    assert x.size == 5, "size is 5"
    assert x.itemsize == 4, "U1 is 4 byte"
    assert x.size * x.itemsize == 20, "array byte size is 20"

    # string (variable length)
    x = np.array(
        ["a", "bb", "ccc", "dddd", "eeeee"]
    )  # en: The length of the string with the maximum length is used
    assert x.dtype == np.dtype("U5")
    assert x.size == 5, "size is 5"
    assert x.itemsize == 20, "U5 is 20 bytes"
    assert x.size * x.itemsize == 100, "array byte size is 100"

    # unicode (fixed length)
    x = np.array(["あ", "い", "う", "え", "お"])
    assert x.dtype == np.dtype("U1")
    assert x.size == 5, "size is 5"
    assert x.itemsize == 4, "U1 is 1 byte"
    assert x.size * x.itemsize == 20, "array byte size is 20"

    # unicode (Emoji ZWJ Sequence)
    # Emoji ZWJ Sequence is a sequence of Unicode characters and
    # ZERO WIDTH JOINER (U+200D) that is used to represent a single emoji.
    # Therefore, the length of a single character is not 1 but 7
    x = np.array(["👨‍👩‍👧‍👦", "👨‍👩‍👧‍👦", "👨‍👩‍👧‍👦", "👨‍👩‍👧‍👦", "👨‍👩‍👧‍👦"])
    assert x.dtype == np.dtype("<U7")
    assert x.size == 5, "size is 5"
    assert x.itemsize == 28, "U7 is 28 bytes"
    assert x.size * x.itemsize == 140, "array byte size is 140"

    # addition of float and int
    # ja: int と float で演算を行う場合に左右の計算順序には関係なく float64 に変換する
    # en: When performing operations on int and float, regardless of order,
    # en: it is converted to float64
    x = np.array([1, 2, 3, 4, 5]) + np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    assert x.dtype == np.float64
    assert x.size == 5, "size is 5"
    assert x.itemsize == 8, "float64 is 8 bytes"
    assert x.size * x.itemsize == 40, "array byte size is 40"
    x = np.array([1.0, 2.0, 3.0, 4.0, 5.0]) + np.array([1, 2, 3, 4, 5])
    assert x.dtype == np.float64
    assert x.size == 5, "size is 5"
    assert x.itemsize == 8, "float64 is 8 bytes"
    assert x.size * x.itemsize == 40, "array byte size is 40"
