import abc
__import__(ABC)

class RegisteredImplementation(object):
    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)


PluginBase.register(RegisteredImplementation)

if __name__ == '__main__':
    print 'Subclass:', issubclass(RegisteredImplementation, PluginBase)
    print 'Instance:', isinstance(RegisteredImplementation(), PluginBase)