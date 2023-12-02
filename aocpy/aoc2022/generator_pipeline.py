"""_Generator Pipeline
"""

class PS:
    def __init__(self, f: callable, *args, **kwargs):
        self.f = f
        self.args = args
        self.kwargs = kwargs


class GeneratorPipeline:
    def __init__(self, gen0):
        self.gen0 = gen0
        self.gen = []

    def pipe(self, f: callable, *args, **kwargs):
        self.gen.append(PS(f, args=args, kwargs=kwargs))

    def __len__(self):
        return len(self.gen)

    def __getitem__(self, position):
        return self.gen[position]

    def __str__(self):
        return str(self.gen)

    def _gpnext(self, idx):
        if 0 == idx:
            return self.gen0
        ps = self.gen[idx - 1]
        return (
            ps.f(self.gen1, *ps.args, **ps.kwargs)
            for gen1 in self._gpnext(idx - 1)
        )

    def __next__(self):
        return self._gpnext(len(self.gen))
        