# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Transforms.RowTakeFilter
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def transforms_rowtakefilter(
        data,
        output_data=None,
        model=None,
        count=9223372036854775807,
        **params):
    """
    **Description**
        Allows limiting input to a subset of rows by taking N first rows.

    :param count: Number of items to take (inputs).
    :param data: Input dataset (inputs).
    :param output_data: Transformed dataset (outputs).
    :param model: Transform model (outputs).
    """

    entrypoint_name = 'Transforms.RowTakeFilter'
    inputs = {}
    outputs = {}

    if count is not None:
        inputs['Count'] = try_set(
            obj=count,
            none_acceptable=False,
            is_of_type=numbers.Real)
    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if output_data is not None:
        outputs['OutputData'] = try_set(
            obj=output_data,
            none_acceptable=False,
            is_of_type=str)
    if model is not None:
        outputs['Model'] = try_set(
            obj=model,
            none_acceptable=False,
            is_of_type=str)

    input_variables = {
        x for x in unlist(inputs.values())
        if isinstance(x, str) and x.startswith("$")}
    output_variables = {
        x for x in unlist(outputs.values())
        if isinstance(x, str) and x.startswith("$")}

    entrypoint = EntryPoint(
        name=entrypoint_name, inputs=inputs, outputs=outputs,
        input_variables=input_variables,
        output_variables=output_variables)
    return entrypoint