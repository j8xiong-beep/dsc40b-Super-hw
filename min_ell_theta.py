def learn_theta(data, colors):
    '''
    Finds theta that is larger than all blue and less than all red.
    '''
    max_blue = max(data[i] for i in range(len(data)) if colors[i] == 'blue')
    min_red = min(data[i] for i in range(len(data)) if colors[i] == 'red')

    return (max_blue + min_red) / 2


def compute_ell(data, colors, theta):
    '''
    Computes the loss function L(theta) for a given theta.
    '''
    loss = 0

    for i in range(len(data)):
        if colors[i] == 'red' and data[i] <= theta:
            loss += 1
        elif colors[i] == 'blue' and data[i] > theta:
            loss += 1

    return loss


def minimize_ell(data, colors):
    '''
    Finds theta that minimizes the loss function L(theta) using quadratic time complexity.
    '''
    best_theta = data[0]
    best_loss = compute_ell(data, colors, best_theta)

    for theta in data:
        current_loss = compute_ell(data, colors, theta)

        if current_loss < best_loss:
            best_loss = current_loss
            best_theta = theta

    return best_theta


def minimize_ell_sorted(data, colors):
    '''
    Finds theta that minimizes the loss function L(theta) in linear time.
    '''
    red_left = 0
    blue_right = colors.count('blue')

    best_loss = red_left + blue_right
    best_theta = data[0] - 1

    for i in range(len(data)):
        if colors[i] == 'blue':
            blue_right -= 1
        elif colors[i] == 'red':
            red_left += 1

        current_loss = red_left + blue_right

        if current_loss < best_loss:
            best_loss = current_loss

            if i == len(data) - 1:
                best_theta = data[i]
            else:
                best_theta = (data[i] + data[i + 1]) / 2

    return best_theta
