from flask import render_template

from sanantonioscientist.extensions import mail


def send_template_message(template=None, ctx=None, *args, **kwargs):
    """
    Send a templated e-mail using a similar signature as Flask-Mail:
    http://pythonhosted.org/Flask-Mail/

    Except, it also supports template rendering. If you want to use a template
    then just omit the body and html kwargs to Flask-Mail and instead supply
    a path to a template. It will auto-lookup and render text/html messages.

    Example:
        ctx = {'user': current_user, 'reset_token': token}
        send_template_message('Password reset from Foo', ['you@example.com'],
                              template='user/mail/password_reset', ctx=ctx)

    Parameters
    ----------
    template : str, optional
        path to template, by default None
    ctx : dict, optional
        context, by default None

    Returns
    -------
    None

    Raises
    ------
    Exception
        Cannot have both template and body arg
    Exception
        Cannot have both template and html arg
    """
    if ctx is None:
        ctx = {}

    if template is not None:
        if 'body' in kwargs:
            raise Exception('You cannot have both a template and body arg.')
        elif 'html' in kwargs:
            raise Exception('You cannot have both a template and html arg.')

        kwargs['body'] = _try_renderer_template(template, **ctx)
        kwargs['html'] = _try_renderer_template(template, ext='html', **ctx)

    mail.send_message(*args, **kwargs)

    return None


def _try_renderer_template(template_path, ext='txt', **kwargs):
    """
    Attempt to render a template.  We use a try/catch here to avoid having to
    do a path exists based on a relative path to the template.

    Parameters
    ----------
    template_path : str
        Template path
    ext : str, optional
        File extension, by default 'txt'

    Returns
    -------
    str
        rendered template string
    """
    try:
        return render_template(f'{template_path}.{ext}', **kwargs)
    except IOError:
        pass
