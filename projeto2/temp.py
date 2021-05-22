def varname(
        frame: int = 1,
        ignore: Optional[IgnoreType] = None,
        multi_vars: bool = False,
        raise_exc: bool = True
) -> Optional[Union[str, Tuple[Union[str, tuple]]]]:
    # Skip one more frame, as it is supposed to be called
    # inside another function
    node = get_node(frame + 1, ignore, raise_exc=raise_exc)
    if not node:
        if raise_exc:
            raise VarnameRetrievingError("Unable to retrieve the ast node.")
        return None

    node = lookfor_parent_assign(node)
    if not node:
        if raise_exc:
            raise VarnameRetrievingError(
                'Failed to retrieve the variable name.'
            )
        return None

    if isinstance(node, ast.AnnAssign):
        target = node.target
    else:
        # Need to actually check that there's just one
        # give warnings if: a = b = func()
        if len(node.targets) > 1:
            warnings.warn("Multiple targets in assignment, variable name "
                          "on the very left will be used.",
                          MultiTargetAssignmentWarning)
        target = node.targets[0]

    names = node_name(target)

    if not isinstance(names, tuple):
        names = (names, )

    if multi_vars:
        return names

    if len(names) > 1:
        raise ImproperUseError(
            f"Expect a single variable on left-hand side, got {len(names)}."
        )

    return names[0]
