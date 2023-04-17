from flask import Flask, jsonify, request
from cases_code import case1, case2

app = Flask(__name__)

pairs = [(10, 3), (2, 3), (3, 6), (5, 6), (5, 17), (4, 5), (4, 8), (8, 9)]
# pairs = list(pairs)


@app.route('/TheAlgorithm',  methods=["POST"])
def func_1():
    childWithNoParents, childWithOneParent = case1.case_1(pairs)
    result = []
    result.append({'child_With_No_Parents': childWithNoParents,
                  'child_With_One_Parent': childWithOneParent})
    return jsonify(
        category="success",
        result=result,
        status=200
    )


@app.route('/Complexrelationships',  methods=["POST"])
def func_2():
    result = []
    nodes = request.args.get("input_nodes")
    nodes = nodes.split(',')
    new_nodes = [int(i) for i in nodes]
    common_ancestors = case2.case_2(pairs, new_nodes)
    result.append({'common_ancestors': common_ancestors})
    return jsonify(
        category="success",
        result=result,
        status=200
    )


if __name__ == "__main__":
    app.run(debug=True)
