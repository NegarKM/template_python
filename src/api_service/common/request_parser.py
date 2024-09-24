parser = {
    "application/x-www-form-urlencoded": lambda req: req.form.to_dict(),
    "application/json": lambda req: req.get_json(),
}


def parse_request_body(r) -> dict:
    return parser.get(r.content_type, lambda x: x.get_data().decode("UTF-8"))(r)
