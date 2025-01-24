import json

from django.http.response import HttpResponseRedirect, JsonResponse
from wagtail_2fa.middleware import VerifyUserPermissionsMiddleware


class NextVerifyUserPermissionsMiddleware(VerifyUserPermissionsMiddleware):
    def process_request(self, request):
        result = super().process_request(request)

        if (
            result
            and isinstance(result, HttpResponseRedirect)
            and "/api/nextjs" in request.path
        ):
            destination = result.url
            html_path = request.GET.get("html_path", None)
            if html_path is not None:
                first_url = destination.split("?next=")[0]
                destination = f"{first_url}?next=/{html_path}"
            data = {
                "redirect": {
                    "destination": destination,
                    "is_permanent": False,
                }
            }
            return JsonResponse(data)

        return result
